import os
import sys
import shutil

class FileOrganizer:
    def __init__(self):
        self.dict_ext = {
            'Images': ['.jpg', '.jpeg', '.png', '.svg'],
            'Python': ['.py'],
            'Text': ['.txt'],
            'Videos': ['.mp4', '.avi', '.mov', '.gif'],
            'Audio': ['.mp3', '.wav', '.flac'],
            'Documents': ['.pdf', '.doc', '.docx', '.xlsx', '.xls', '.csv', '.json'],
            'Compressed': ['.zip', '.rar'],
            'Others': []
        }

        if len(sys.argv) != 2:
            print("❌ Usage: python file_organizer.py <source_folder>")
            sys.exit()

        self.source_folder = sys.argv[1]

        if not os.path.exists(self.source_folder):
            print("❌ Source folder does not exist.")
            sys.exit()

        self.organize_files()

    def get_category(self, ext):
        for category, extensions in self.dict_ext.items():
            if ext.lower() in extensions:
                return category
        return 'Others'

    def organize_files(self):
        for file in os.listdir(self.source_folder):
            file_path = os.path.join(self.source_folder, file)

            if os.path.isfile(file_path):
                ext = os.path.splitext(file)[1]
                category = self.get_category(ext)
                category_path = os.path.join(self.source_folder, category)

                if not os.path.exists(category_path):
                    os.makedirs(category_path)

                new_path = os.path.join(category_path, file)

                print(f"📁 Moving: {file} → {category}/")
                shutil.move(file_path, new_path)


if __name__ == "__main__":
    FileOrganizer()
