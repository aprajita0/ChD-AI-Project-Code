import os
import shutil
import pydicom

# Define source and destination
src_patient_folder = r"C:\Users\ankes\Desktop\ChD-AI Project-Code\PAT23-PED-MRI_017Y"
dst_folder = r"C:\Users\ankes\Desktop\ChD-AI Project-Code\Patient27_ModelData"

# Helper: to find series does that contain "cine" 
def is_cine_series(description):
    return description and "cine" in description.lower()

os.makedirs(dst_folder, exist_ok=True)

# We'll go through each series folder for patient
for series_folder in os.listdir(src_patient_folder):
    full_series_path = os.path.join(src_patient_folder, series_folder)

    if os.path.isdir(full_series_path):
        try:
            # We will just check the first DICOM file in the series as we dont need to look ar all
            for file in os.listdir(full_series_path):
                if file.lower().endswith(".dcm"):
                    dcm_path = os.path.join(full_series_path, file)
                    ds = pydicom.dcmread(dcm_path, stop_before_pixels=True)
                    desc_element = ds.get((0x0008, 0x103E), "")
                    desc = str(desc_element.value) if hasattr(desc_element, 'value') else str(desc_element)
                    if is_cine_series(desc):
                        print(f" CINE Series Found: '{desc}' → {series_folder}")
                        dst_series_path = os.path.join(dst_folder, series_folder)
                        shutil.copytree(full_series_path, dst_series_path, dirs_exist_ok=True)
                    break  
        except Exception as e:
            print(f"Error processing {series_folder}: {e}")

print("All CINE series moved to:", dst_folder)
