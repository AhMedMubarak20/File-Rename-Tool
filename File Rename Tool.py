import os

def rename_files(directory, prefix):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            new_filename = f"{prefix}_{filename}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed {filename} to {new_filename}")

folder_path = input("Enter folder path: ")
new_prefix = input("Enter new filename prefix: ")
rename_files(folder_path, new_prefix)
