# Folder Organizer

A simple Python script to organize files into folders based on their extensions. This script moves files from a source directory to a destination directory, creating subfolders named after each file extension.

## Features

- Organizes files into subfolders named after their extensions.
- Copies files while preserving their metadata.
- Handles permissions errors gracefully.
- Recursively processes subdirectories.

## Requirements

- Python 3.12

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/folder-organizer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd folder-organizer
    ```

## Usage

1. Run the script:

    ```bash
    python cleaner.py
    ```

2. Follow the prompts to enter the source and destination paths:

    ```text
    Enter the path to move the files from: /path/to/source
    Enter the path to move the files to: /path/to/destination
    ```

## Example

For example, if you have a source directory `/path/to/source` containing the following files:

```text
source
├── document1.txt
├── image1.jpg
└── subfolder
    └── document2.txt
```

And you specify  `/path/to/destination` as the destination directory, the script will create the following structure:

```text
destination
├── txt
│   ├── document1.txt
│   └── document2.txt
└── jpg
    └── image1.jpg
```

## Note 

- Ensure you have the necessary read/write permissions for both the source and destination directories.
- This script is designed to move files. Modify shutil.move to shutil.copy2 if you want to copy files instead of moving


## License

This project is licensed under the MIT License. See the LICENSE file for details.

```text

This `README.md` file should give users a clear understanding of what the project does, how to install and use it, and provide some context about the code and its features.

```



