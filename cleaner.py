import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


#folder for keeping files
download_folder = 'C:/Users/sadiq/Downloads'

class DownloadOrganizer(FileSystemEventHandler):
    ...

    def __init__(self,dest_folder):
        self.dest_folder = dest_folder

    def scan(self):

        source_path = ''
        
        # spliting into filename and extension
        filename, extension = os.path.splitext(source_path)

        # Creating subfolders path for a particular file type 
        extension_folder = os.path.join(self.dest_folder,extension.lstrip('.'))

        # creating the subfolders if it does not exits
        os.makedirs(extension_folder,exit_ok= True)

        dest_path = os.path.join(self.dest_folder, filename + extension)
        shutil.copy2(source_path,dest_path)
        print(f" Copied {filename}{extension} to {extension_folder}")
        

def main():
    ...


if __name__ == '__main__':
    main()