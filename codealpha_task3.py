import os
import shutil

def file_organize(directory):
    # Checking if the directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return
    # Geting all the files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file in files:
        # Geting the file extension - 
        Extension = file.split('.')[-1]
        
        # Creating a subdirectory for the file extension if it doesn't exist
        extension_dir = os.path.join(directory, Extension)
        if not os.path.exists(extension_dir):
            os.makedirs(extension_dir)
        
        # Moveing  the file to the extension directory - 
        src_path = os.path.join(directory, file)
        dst_path = os.path.join(extension_dir, file)
        shutil.move(src_path, dst_path)
        print(f"Moved {file} to {extension_dir}")

# Executinng - 
directory_to_organize = r'C:\Users\Shree Ji\Desktop\Codealpha Projects'
file_organize(directory_to_organize)
