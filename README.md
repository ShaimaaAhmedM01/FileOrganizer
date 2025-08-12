# FileOrganizer

## Overview:
Python script to organize files in a given folder into subfolders based on their file types.

## Features:
- Organizes files into predefined categories:
  - Images
  - Documents
  - Videos
  - Archives
  - Code
  - Others (for unknown file types)
- **Simulation Mode**: Shows what would happen without moving any files.
- Displays a summary of how many files were moved into each category.

## How It Works
1. The script asks for the folder path containing your files.
2. It scans only the top-level folders (ignores subfolders).
3. Based on the file extension, it moves each file into the appropriate category folder.
4. If the category folder does not exist, it is created automatically.
5. If simulation mode is enabled, files are not moved — only the planned moves are shown.

## Requirements
- Python 3.x (Tested with Python 3.10)
- No extra libraries required (uses built-in Python modules: `os`, `shutil`)

### 1. Clone or download this repository
- git clone https://github.com/ShaimaaAhmedM01/FileOrganizer.git
- cd FileOrganizer

## Run script
python FileOrganizer.py

## Example Output 
- Please type in the full path of the folder containing your files: /Users/shaimaa/Desktop/test
- Do you want to run in simulate mode? (yes/no): yes
- Simulation mode ON — No files will be moved.
- [SIMULATE] Would move 'photo.jpg' → 'Images/'
- [SIMULATE] Would move 'report.pdf' → 'Documents/'

Summary:
Images: 1
Documents: 1
Videos: 0
Audio: 0
Archives: 0
Code: 0
Others: 0
