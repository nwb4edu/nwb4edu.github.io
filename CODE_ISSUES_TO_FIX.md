# Code Execution Issues to Fix

Based on JOSE review feedback (Issues #4 and #8), the following code execution errors need to be addressed:

## Lesson 2: Large-scale Electrophysiology

### Lesson_2/02-Visualizing_Recordings.ipynb
- **Cell 2**: Name error
- **Function definitions**: Spacing issues (PEP8 compliance needed)
- **Function names**: Some use CamelCase instead of snake_case
- **Docstrings**: Inconsistent numpy-style docstrings

## Lesson 3: Single-cell Electrophysiology

### Lesson_3/02-Analyzing_Computed_Features.ipynb
- **Cell 2**: Keyboard interrupt (probably a timeout issue)

## Lesson 4: Two-photon Calcium Imaging

### Lesson_4/01-Retrieving_Brain_Observatory_Data.ipynb
- **Last cell**: Index error

## Lesson 5: Greatest Hits

### Lesson_5/01-PlaceFields.ipynb
- **Last cell**: Keyboard interrupt (timeout)
- **autocorrelation_function**: Rendering error

### Lesson_5/02-RotationalDynamics.ipynb
- **Cell 4**: Keyboard interrupt (timeout)
- **Later cells**: Prints excessively large array (needs output suppression or limiting)

## Additional Code Style Issues

### General Python Code Style (across all lessons)
- [ ] Improve PEP8 compliance throughout
- [ ] Standardize function naming (use snake_case, not CamelCase)
- [ ] Add consistent numpy-style docstrings to all functions
- [ ] Fix spacing issues in function definitions
- [ ] Ensure proper spacing around operators and after commas
- [ ] Keep lines under 100 characters when possible

### Setup Page
- [x] Fixed: Typo in code block (`!pip install pwynb` → `!pip install pynwb`)
- [ ] Fix: Last code block prints an unintentional error message

## Testing Checklist

Before marking these issues as resolved:
1. [ ] Run all cells in each affected notebook in order
2. [ ] Verify no errors occur
3. [ ] Check that all figures display properly
4. [ ] Ensure outputs are reasonable (not excessively large)
5. [ ] Verify data files are accessible
6. [ ] Test on JupyterHub/DandiHub if possible
7. [ ] Build Jupyter Book and check rendered output

## Notes

- Some timeout issues may be related to data download sizes or computation time
- Consider adding progress bars or status messages for long-running cells
- For large array outputs, consider using `print(array.shape)` instead of printing the full array
- All file paths should be verified to work both locally and on JupyterHub
