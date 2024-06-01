import os
from pathlib import Path
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


#folder for keeping files
download_folder_path = 'C:/Users/sadiq/Downloads'
dest_folder_path = "C:/filesFromDownloads"

def folder_scanner(path=Path()):
    for entry in path.iterdir():
        if entry.is_file():
            full_name = os.path.basename(entry)
            file = os.path.splitext(full_name)
            filename = file[0]
            extension = file[1]

            extension_folder_path = os.path.join(dest_folder_path,extension.lstrip('.')) 
            os.makedirs(extension_folder_path,exist_ok=True) # creating folders based on extensions


        elif entry.is_dir():
            folder_scanner(entry)



# def transfer_files(filename,extension):
#     ...
#     extension_folder = os.path.join(dest_folder_path,extension.lstrip('.'))
#     print(extension_folder)


folder_scanner(path=Path(download_folder_path))
# transfer_files(filename,extension)


    




# class DownloadOrganizer(FileSystemEventHandler):
#     ...

#     def __init__(self,dest_folder):
#         self.dest_folder = dest_folder

#     def scan(self):

#         source_path = ''
        
#         # spliting into filename and extension
#         filename, extension = os.path.splitext(source_path)

#         # Creating subfolders path for a particular file type 
#         extension_folder = os.path.join(self.dest_folder,extension.lstrip('.'))

#         # creating the subfolders if it does not exits
#         os.makedirs(extension_folder,exit_ok= True)

#         dest_path = os.path.join(self.dest_folder, filename + extension)
#         shutil.copy2(source_path,dest_path)
#         print(f" Copied {filename}{extension} to {extension_folder}")
        

def main():
    ...


if __name__ == '__main__':
    main()