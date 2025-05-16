import pickle
import os
import time  
import datetime
import csv
import shutil
from pathlib import Path

class FileBackupManager:
    def __init__(self, source, backup):
        self.source_path = Path(source)
        self.backup_path = Path(backup)
        self.backup_path_creating()
        self.scaning_folders()
        self.report_saving_csv()
        self.copy_all_files_to_temp()
        self.backup_archive()

    def backup_path_creating(self):
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        self.filename = f"backup_{timestamp}"
        self.report_folder_name = f"Backup_Reports_{timestamp}"
        self.temp_dir = self.backup_path / self.report_folder_name
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        self.temp_files_dir = self.temp_dir / "Files"
        self.temp_files_dir.mkdir(parents=True, exist_ok=True)
        print(f"📁 Temp folder created: {self.temp_dir}")

    def scaning_folders(self):
        num = 0
        self.logs = []
        self.csv_list = []
        for root, dirs, files in os.walk(self.source_path):
            for file_name in files:
                scanning_path = Path(root) / file_name
                num += 1
                self.csv_list.append(scanning_path)
                log = f"{num}. 📁 Scanning: {scanning_path}"
                self.logs.append(log)
                print(log)
        print(f"📄 {num} files found!")

    def report_saving_csv(self):
        heading = ['Name', 'Size', 'File type', 'Last modified']
        csv_items = []
        csv_file = self.temp_dir / "Report.csv"
        pickle_file = self.temp_dir / "Report.pkl"

        with open(pickle_file, 'wb') as pk:
            pickle.dump(self.logs, pk)

        with open(csv_file, 'w', newline='', encoding="utf-8") as f:
            writ = csv.writer(f)
            writ.writerow(heading)
            for scanning_path in self.csv_list:
                file_name = scanning_path.stem
                file_ext = scanning_path.suffix.lstrip('.')
                modified_time = os.path.getmtime(scanning_path)
                modified_date = datetime.datetime.fromtimestamp(modified_time).strftime("%d-%m-%Y %I:%M %p") 
                size = f"{scanning_path.stat().st_size} Bytes"
                data = [file_name, size, file_ext, modified_date]
                writ.writerow(data)

    def copy_all_files_to_temp(self):
        print("📥 Copying files to temp folder...")
        for path in self.csv_list:
            relative = path.relative_to(self.source_path)
            destination = self.temp_files_dir / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, destination)
        print("✅ Files copied successfully.")

    def backup_archive(self):
        t1 = time.time()
        try:
            print("📦 Creating zip archive...")
            zip_path = self.backup_path / self.filename
            shutil.make_archive(str(zip_path), 'zip', root_dir=self.temp_dir)
            print(f"✅ Backup succeeded: {zip_path}.zip")
        except Exception as e:
            print(f"❌ Failed to backup: {e}")
        finally:
            shutil.rmtree(self.temp_dir)
            print(f"🧹 Temp folder deleted: {self.temp_dir}")
        t2 = time.time()
        print(f"⏱️ Backup took: {round(t2 - t1, 2)} seconds.")

# ------------------ Run -------------------
source_path = r"D:\Bijay\tally pdf"
backup_path = r"D:\Bijay\test"
        
if __name__ == "__main__":
    FileBackupManager(source=source_path, backup=backup_path)
