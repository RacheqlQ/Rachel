"""
This is production engineering. The purpose is to automatically check:
Detection datasets:
- image exists
- label exists
- coordinates valid
- class ids valid
- image not corrupt

Segmentation datasets:
- image count == mask count
- matching filenames
- image dimensions valid
- masks readable

I should be able to run:
`python src/preprocessing/dataset_validation.py` and get:
Dataset Validation Report

✓ Images: 4139

✓ Labels: 4139

✓ Missing Files: 0

✓ Invalid Labels: 0

✓ Corrupt Images: 0
"""
