# This becomes important because the datasets come from different sources.

# AURA-X Taxonomy Mapping

| Dataset Class | AURA-X Class |
|--------------|--------------|
| crack | structural_defect |
| dent | structural_defect |
| paint-off | surface_degradation |
| scratch | surface_degradation |
| bad weld | weld_defect |
| defect | weld_defect |

## Note: Without this file, we may end up training models with inconsistent labels.