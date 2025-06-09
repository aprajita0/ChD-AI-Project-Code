# CINE Series Filtering Script for DICOM Data

This script filters cardiac MRI series that contain the word **"CINE"** in their DICOM Series Description field and copies them into a new folder for further analysis or machine learning processing.

## Requirements

- Python 3.7+
- `pydicom` library

Install dependencies with:

```bash
pip install pydicom
```

## Usage

1. Open the script `filtering_data_for_model.py`.
2. Update the following variables:

```python
src_patient_folder = r"PATH/TO/PATIENT_FOLDER"     # Path to the folder containing all series
dst_folder = r"PATH/TO/DESTINATION_FOLDER"         # Path where matching series will be copied
```

3. Run the script using the terminal or command prompt:

```bash
python filtering_data_for_model.py
```

The script will create the destination folder if it does not exist and copy all series folders that contain "CINE" in their Series Description.

## Notes

- Only the first DICOM file in each series folder is read to check the description.
- The script assumes each series is stored in its own subfolder.
- No modifications are made to the original data.