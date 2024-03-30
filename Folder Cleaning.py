import os
import pandas as pd

# Path to the Excel file
excel_path = '/path/to/your/excel_file.xlsx'

# Load the Excel file
df = pd.read_excel(excel_path)

# Concatenate file paths from all columns into a single list, ensuring strings only
file_paths_from_excel = pd.concat([df[col] for col in df.columns if df[col].dtype == 'object']).dropna().tolist()

# Preprocess file paths: remove '/upload' if it's at the beginning of the path
file_paths_from_excel = [path.lstrip('/upload') for path in file_paths_from_excel]

# The root folder to check
root_folder = '/path/to/upload'

# Function to get relative path
def get_relative_path(full_path, base_path):
    return os.path.relpath(full_path, base_path)

# Traverse the root_folder
for root, dirs, files in os.walk(root_folder):
    for file in files:
        # Full path of the current file
        file_full_path = os.path.join(root, file)
        
        # Get the relative path of the file to the 'upload' folder
        relative_path = get_relative_path(file_full_path, root_folder)
        
        # Check if the relative path is not in the list from the Excel file
        if relative_path not in file_paths_from_excel:
            # Delete the file
            os.remove(file_full_path)
            print(f"Deleted: {file_full_path}")
