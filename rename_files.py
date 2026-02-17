import os

folder_path = "path_to_your_folder"

for index, filename in enumerate(os.listdir(folder_path)):
    file_extension = filename.split(".")[-1]
    new_name = f"file_{index}.{file_extension}"
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)

print("Files renamed successfully.")
