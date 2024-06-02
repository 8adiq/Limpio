import os
from pathlib import Path
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


#folder for keeping files
download_folder_path = 'C:/Users/sadiq/Downloads'
dest_folder_path = "C:/filesFromDownloads"

def folder_organizer(path=Path()):
    for entry in path.iterdir():
        if entry.is_file():
            full_name = os.path.basename(entry)
            file = os.path.splitext(full_name)
            filename = file[0]
            extension = file[1]

            extension_folder_path = os.path.join(dest_folder_path,extension.lstrip('.')) 
            os.makedirs(extension_folder_path,exist_ok=True) # creating folders based on extensions

            final_file_path = os.path.join(extension_folder_path, filename + extension)
            shutil.move(entry,final_file_path)
            print(f'filename {filename} has been copied to {dest_folder_path}')


        elif entry.is_dir():
            folder_organizer(entry)


folder_organizer(path=Path(download_folder_path))

        

def main():
    ...


if __name__ == '__main__':
    main()