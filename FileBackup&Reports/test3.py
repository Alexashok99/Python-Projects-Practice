
#------------------------------File Manager + Backup & Report System-----------------------
# एक ऐसा Python टूल बनाएँ जो किसी फोल्डर के अंदर:

# सभी फाइलों का रिकॉर्ड बनाए

# उनकी डिटेल्स को CSV/JSON में सेव करे

# उनका बैकअप बनाए

# टाइम और तारीख के साथ रिपोर्ट जनरेट करे

# और user interaction के लिए CLI मेनू दे


# import sys
# import random
# import math
# import json
import pickle
import os
import time  
import datetime
import csv
import shutil
from pathlib import Path

class FileBackupManager:
    def __init__(self, source, backup):
        self.source_path = source
        self.backup_path = backup
        self.backup_path_creating()
        self.scaning_folders()
        self.report_saving_csv()
        self.backup_archive()

    def backup_path_creating(self):
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        self.filename = f"backup_{timestamp}"
        self.report_folder_name = f"Backup_Reports_{timestamp}"
        self.temp_dir = Path(os.path.join(self.backup_path, self.report_folder_name))
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        print(f"📁 Temp report folder created: {self.temp_dir}")


    def scaning_folders(self):
        num = 0
        self.logs = []
        self.csv_list = []
        scanned = os.walk(self.source_path)
        for root, dirs , files in scanned:
            for file_name in files:
                scanning_path = os.path.join(root, file_name)
                num +=1
                self.csv_list.append(scanning_path)
                log = f"{num}. 📁 Scanning folder: {scanning_path} >>> :"
                self.logs.append(log)
                print(log)
        print(f"📄 {num} files found !")

    def report_saving_csv(self):
        heading = ['Name', 'Size', 'File type', 'Last modified']
        csv_items = []
        csv_file = os.path.join(self.temp_dir, "Report.csv")
        # pickle_file = os.path.join(self.backup_folder, "Report.pkl")
        pickle_file = os.path.join(self.temp_dir, "Report.pkl")
        # nn = Path(pickle_file).mkdir(parents=True, exist_ok=True)
        with open(pickle_file, '+bw') as pk:
            pickle.dump(self.logs, pk)
        with open(csv_file, 'w', newline='') as f:
            writ = csv.writer(f)
            writ.writerow(heading)
        for scanning_path in self.csv_list:
            file_name = Path(scanning_path).stem
            file_ext = Path(scanning_path).suffix.lstrip('.')
            modifeided_time = os.path.getmtime(scanning_path)
            modifeided_date = datetime.datetime.fromtimestamp(modifeided_time).strftime("%d-%m-%Y %I:%M %p") 
            sizes = f"{Path(scanning_path).stat().st_size} Bytes"
            data = [file_name, sizes, file_ext, modifeided_date]
            csv_items.append(data)
        with open(csv_file, 'a', encoding="utf-8", newline='') as f:
            writ = csv.writer(f)
            for i in csv_items:
                writ.writerow(i)
        
    # def backup_archive(self):
    #     t1 = time.time()
    #     try:
    #         print("📦 Backuping...")
    #         shutil.make_archive(str(self.backup_folder), 'zip', root_dir=self.backup_folder) #chatgpt
    #         print(f"✅ Backup succeeded: {self.backup_folder}.zip")
    #     except Exception as e:
    #         print(f"❌ Failed to backup: {e}")
    #     t2 = time.time()
    #     print(f"⏱️ Backup took: {round(t2 - t1, 2)} seconds.")

    def backup_archive(self):
        t1 = time.time()
        try:
            print("📦 Creating zip archive...")
            zip_path = os.path.join(self.backup_path, self.filename)
            shutil.make_archive(zip_path, 'zip', root_dir=self.temp_dir.parent, base_dir=self.temp_dir.name)
            print(f"✅ Backup succeeded: {zip_path}.zip")
        except Exception as e:
            print(f"❌ Failed to backup: {e}")
        finally:
            # Cleanup: remove temp folder after creating zip
            shutil.rmtree(self.temp_dir)
            print(f"🧹 Temp folder deleted: {self.temp_dir}")
        t2 = time.time()
        print(f"⏱️ Backup took: {round(t2 - t1, 2)} seconds.")


source_path = r"D:\Bijay\tally pdf"
backup_path = r"D:\Bijay\test"
        
# if __name__ == "__main__":
#     FileBackupManager(source=source_path, backup=backup_path)


# with open('Report.pkl', 'rb') as f:
#     loaded_data = pickle.load(f)
# print(loaded_data)