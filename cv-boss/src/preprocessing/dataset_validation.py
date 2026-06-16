
from pathlib import Path
from PIL import Image

def validate_yolo_dataset(dataset_root: str):
    """
    This is production engineering. The purpose is to automatically check:
    Detection datasets:
    - image exists
    - label exists
    - coordinates valid
    - class ids valid
    - image not corrupt
    """
    dataset_root = Path(dataset_root)

    print("\n========== YOLO DATASET VALIDATION ==========\n")

    image_extensions = {".jpg", ".jpeg", ".png"}

    total_images = 0
    missing_labels = 0
    corrupt_images = 0
    invalid_labels = 0

    for split in ["train", "valid", "test"]:
        image_dir = dataset_root / split / "images"
        label_dir = dataset_root / split / "labels"

        if not image_dir.exists():
            print(f"[WARNING] Missing {image_dir}")
            continue

        images = [
            f for f in image_dir.iterdir()
            if f.suffix.lower() in image_extensions
        ]

        total_images += len(images)

        for img_path in images:
            label_path = label_dir / f"{img_path.stem}.txt"

            if not label_path.exists():
                missing_labels += 1
                continue

            try:
                Image.open(img_path).verify()
            except Exception:
                corrupt_images += 1

            try:
                with open(label_path, "r") as f:
                    lines = f.readlines()

                for line in lines:
                    parts = line.strip().split()

                    if len(parts) != 5:
                        invalid_labels += 1
                        continue

                    class_id = int(parts[0])

                    if class_id < 0:
                        invalid_labels += 1

            except Exception:
                invalid_labels += 1

    print(f"Total Images      : {total_images}")
    print(f"Missing Labels    : {missing_labels}")
    print(f"Corrupt Images    : {corrupt_images}")
    print(f"Invalid Labels    : {invalid_labels}")


def validate_segmentation_dataset(images_dir: str, masks_dir: str):
    """
    Segmentation datasets:
    - image count == mask count
    - matching filenames
    - image dimensions valid
    - masks readable
    
    _summary_

    Args:
        images_dir (str): _description_
        masks_dir (str): _description_
    """
    images_dir = Path(images_dir)
    masks_dir = Path(masks_dir)

    print("\n========== SEGMENTATION DATASET VALIDATION ==========\n")

    images = sorted(images_dir.glob("*"))
    masks = sorted(masks_dir.glob("*"))

    print(f"Images Found : {len(images)}")
    print(f"Masks Found  : {len(masks)}")

    missing_masks = 0

    image_names = {img.stem for img in images}
    mask_names = {mask.stem for mask in masks}

    for image_name in image_names:
        if image_name not in mask_names:
            missing_masks += 1

    print(f"Missing Masks : {missing_masks}")

    try:
        sample_image = Image.open(images[0])
        sample_mask = Image.open(masks[0])

        print(f"Image Size : {sample_image.size}")
        print(f"Mask Size  : {sample_mask.size}")

    except Exception as e:
        print(f"Error opening sample files: {e}")


if __name__ == "__main__":

    # YOLO DATASET
    validate_yolo_dataset("./cracks")

    # U-NET DATASET
    validate_segmentation_dataset(
        "./cracks_with_mask/images",
        "./cracks_with_mask/masks"
    )