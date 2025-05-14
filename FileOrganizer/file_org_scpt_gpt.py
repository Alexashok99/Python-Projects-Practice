
"""
File Organizer Script
----------------------

This script organizes files in a given folder based on their file extensions.
It scans all files inside the specified directory and moves them into categorized folders
such as Images, Documents, Videos, Audio, Python files, etc.

How it works:
1. The user provides the target folder path as a command-line argument.
2. The script loops through all files in that folder.
3. It checks the extension of each file and determines its category.
4. It creates a new folder for that category (if it doesn’t exist).
5. Then it copies the file into the appropriate folder.

Features:
- Supports common file types like .jpg, .pdf, .mp3, .zip, etc.
- Automatically handles unknown types by moving them into an "Others" folder.
- Uses shutil.copy2() to retain original file metadata.
- Provides basic error handling for invalid paths.

Usage:
    python file_org_scpt_gpt.py "C:\\Users\\YourName\\Downloads"

This tool helps keep directories clean and well-organized automatically.
"""
#-------------------USE COMMAND---------------------
# python file_org_scpt_gpt.py "E:\Your\Folder\Path"
#----------------------CODE-------------------------
import os
import sys
import shutil

class FileOrganizer:
    def __init__(self):       
        self.dict_ext = {
            'Image': ['.jpg', '.jpeg', '.png', '.svg'],
            'Python': ['.py'],
            'Text': ['.txt'],
            'Videos': ['.mp4', '.avi', '.mov', '.gif'],
            'Audio': ['.mp3', '.wav', '.flac'],
            'Document': ['.pdf', '.doc', '.docx', '.xlsx', '.xls', '.csv', '.json', '.js'],
            'Compressed': ['.zip', '.rar'],
            'Others': []
        }

        if len(sys.argv) < 2:
            print("❌ Usage: python file_organizer.py <folder_path>")
            sys.exit(1)

        self.source_folder = sys.argv[1]

        if not os.path.isdir(self.source_folder):
            print("❌ Provided path is not a directory.")
            sys.exit(1)

        self.file_dir()

    def get_category(self, ext):
        for category, extensions in self.dict_ext.items():
            if ext.lower() in extensions:
                return category
        return 'Others'

    def file_dir(self):
        for file_name in os.listdir(self.source_folder):
            src_path = os.path.join(self.source_folder, file_name)
            if os.path.isfile(src_path):
                ext = os.path.splitext(file_name)[1]
                category = self.get_category(ext)
                dest_folder = os.path.join(self.source_folder, category)

                os.makedirs(dest_folder, exist_ok=True)
                dest_path = os.path.join(dest_folder, file_name)

                print(f"📦 Copying {file_name} → {category}/")
                shutil.copy2(src_path, dest_path)  # keeps metadata too

if __name__ == "__main__":
    FileOrganizer()
