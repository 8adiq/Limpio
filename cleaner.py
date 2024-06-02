import os
from pathlib import Path
import shutil

def folder_organizer(dest_path,path=Path()):
    for entry in path.iterdir():
        if entry.is_file():
            if os.access(entry, os.R_OK) and os.access(dest_path, os.W_OK):
                try:
                    full_name = os.path.basename(entry)
                    filename, extension = os.path.splitext(full_name)

                    extension_folder_path = os.path.join(dest_path,extension.lstrip('.')) 
                    os.makedirs(extension_folder_path,exist_ok=True) 

                    final_file_path = os.path.join(extension_folder_path, filename + extension)
                    shutil.copy2(entry,final_file_path)
                    print(f'{filename} has been copied to {extension_folder_path}')
                except PermissionError as e:
                    print(f" Permission denied for copying {filename} - {e}")
                except Exception as e:
                    print(f" Error copying {filename} - {e}")
            else:
                print(f" No read/write permission for copying {filename}")

        elif entry.is_dir():
            folder_organizer(dest_path,path=Path(entry))    

def main():
    source_path = input("Enter the path to move the file from ").strip()
    dest_path = input(" Enter the path to move the files to ").strip()

    if not os.path.exists(dest_path):
        os.makedirs(dest_path,exist_ok=True)

    folder_organizer(dest_path,path=Path(source_path))

if __name__ == '__main__':
    main()






#folder for keeping files
download_folder_path = "C:/filesFromDownloads"
dest_folder_path = "C:/filesFromDocuments"

