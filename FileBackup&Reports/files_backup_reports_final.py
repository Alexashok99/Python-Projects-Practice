
#------------------------------File Manager + Backup & Report System-----------------------
# एक ऐसा Python टूल बनाएँ जो किसी फोल्डर के अंदर:

# सभी फाइलों का रिकॉर्ड बनाए

# उनकी डिटेल्स को CSV/JSON में सेव करे

# उनका बैकअप बनाए

# टाइम और तारीख के साथ रिपोर्ट जनरेट करे

# और user interaction के लिए CLI मेनू दे

# 🔍 Filter by file type / size

# 📁 GUI version with folder picker

# 🔔 Email / Notification on completion



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
        self.backup_path_creating()     # 🏗️ Create temp backup folder
        self.scaning_folders()          # 🔍 Scan and collect all files
        self.report_saving_csv()        # 📝 Save reports as CSV + Pickle
        self.copy_all_files_to_temp()   # 📥 Copy files to temp folder
        self.backup_archive()           # 📦 Create zip archive of everything

    def backup_path_creating(self):
        """🛠️ Temporary folder create karta hai jahan backup aur report save honge."""
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        self.filename = f"backup_{timestamp}"  # Final zip filename
        self.report_folder_name = f"Backup_Reports_{timestamp}"  # Temp folder name
        self.temp_dir = self.backup_path / self.report_folder_name
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        self.temp_files_dir = self.temp_dir / "Files"
        self.temp_files_dir.mkdir(parents=True, exist_ok=True)
        print(f"📁 Temp folder created: {self.temp_dir}")

    def scaning_folders(self):
        """📂 Source folder ke sare files ko scan karke list me store karta hai."""
        self.logs = []
        self.csv_list = []
        for num, (root, _, files) in enumerate(os.walk(self.source_path), start=1):
            for file_name in files:
                path = Path(root) / file_name
                self.csv_list.append(path)
                log = f"{len(self.csv_list)}. 📁 Scanning: {path}"
                self.logs.append(log)
                print(log)
        print(f"📄 {len(self.csv_list)} files found!")

    def report_saving_csv(self):
        """📄 Report.csv aur Report.pkl file save karta hai with file details."""
        csv_file = self.temp_dir / "Report.csv"
        pickle_file = self.temp_dir / "Report.pkl"

        # 🧾 Pickle log report save
        with open(pickle_file, 'wb') as pk:
            pickle.dump(self.logs, pk)

        # 📊 CSV report save
        with open(csv_file, 'w', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Size', 'File type', 'Last modified'])

            for path in self.csv_list:
                name = path.stem
                ext = path.suffix.lstrip('.')
                size = f"{path.stat().st_size} Bytes"
                modified = datetime.datetime.fromtimestamp(path.stat().st_mtime).strftime("%d-%m-%Y %I:%M %p")
                writer.writerow([name, size, ext, modified])

    def copy_all_files_to_temp(self):
        """📥 Sare scanned files ko temp folder me copy karta hai original structure ke sath."""
        print("📥 Copying files to temp folder...")
        for path in self.csv_list:
            relative = path.relative_to(self.source_path)
            destination = self.temp_files_dir / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, destination)
        print("✅ Files copied successfully.")

    def backup_archive(self):
        """📦 Temp folder ko zip me convert karta hai, aur temp folder delete karta hai."""
        t1 = time.time()
        zip_path = self.backup_path / self.filename

        try:
            print("📦 Creating zip archive...")
            shutil.make_archive(str(zip_path), 'zip', root_dir=self.temp_dir)
            print(f"✅ Backup succeeded: {zip_path}.zip")
        except Exception as e:
            print(f"❌ Failed to backup: {e}")
        finally:
            shutil.rmtree(self.temp_dir)  # 🧹 Cleanup temp folder
            print(f"🧹 Temp folder deleted: {self.temp_dir}")
        
        print(f"⏱️ Backup took: {round(time.time() - t1, 2)} seconds.")

# ------------------ Run -------------------
source_path = r"E:\BIJAY\python\PYTHON\Moduel"
backup_path = r"D:\Bijay\test"

if __name__ == "__main__":
    FileBackupManager(source=source_path, backup=backup_path)
