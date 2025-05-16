
#------------------------------File Manager + Backup & Report System-----------------------
# एक ऐसा Python टूल बनाएँ जो किसी फोल्डर के अंदर:

# सभी फाइलों का रिकॉर्ड बनाए

# उनकी डिटेल्स को CSV/JSON में सेव करे

# उनका बैकअप बनाए

# टाइम और तारीख के साथ रिपोर्ट जनरेट करे

# और user interaction के लिए CLI मेनू दे


# import sys
import os
import time  
import datetime
# import random
# import math
# import json
import csv
# import pickle
import shutil
from pathlib import Path



# scan_path = input(r"Enter Path For Backup: ").strip()
# num = 0
# scanned = os.walk(scan_path)
# for root, dirs , files in scanned:
#     # print(root)
#     for file_name in files:
#         scanning_path = os.path.join(root, file_name)
#         num +=1
#         # print(f"📁 Scanning folder: {scanning_path} >>> {num}")
#         names_types = os.path.basename(scanning_path).split('.')
#         # bb = os.path.splitext(scanning_path)[1]
#         # print(names_types[0], names_types[1])
#         modifeided_time = os.path.getmtime(scanning_path)
#         formats = time.strftime("%d-%m-%Y %H:%M %p", time.localtime(modifeided_time))
#         bb = datetime.datetime.fromtimestamp(modifeided_time).strftime("%d-%m-%Y %I:%M %p") 
        
        # print(formats)
        # print(bb, formats)

scan_path = r"D:\Bijay\tally pdf"
backup_path = r"D:\Bijay\test"

def backup_path_creating():
    global backup_folder
    filename = f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    backup_folder = Path().joinpath(backup_path, filename)
    # print(backup_folder)
    if not os.path.exists(backup_folder):
        Path(backup_folder).mkdir(parents=True, exist_ok=True)
        print(f"File Created in <<{backup_path}>> of Name: <<{filename}>>")
    else:
        print(f"File Exists in <<{backup_path}>> of Name: <<{filename}>>")
        
def scaning_folders():
    global num, lst
    num = 0
    lst = []
    scanned = os.walk(scan_path)
    for root, dirs , files in scanned:
        for file_name in files:
            scanning_path = os.path.join(root, file_name)
            num +=1
            lst.append(scanning_path)
            print(f"📁 Scanning folder: {scanning_path} >>> {num}")
    # print(lst)
    print(f"📄 {num} files found")


def report_saving_csv():
    backup_path_creating()
    scaning_folders()
    heading = ['Name', 'Size', 'File type', 'Last modified']
    npath = os.path.join(backup_folder, "Report.csv")
    with open(npath, 'w', newline='') as f:
        writ = csv.writer(f)
        writ.writerow(heading)
    for scanning_path in lst:
        # names_types = os.path.basename(scanning_path).split('.')
        file_name = Path(scanning_path).stem
        file_ext = Path(scanning_path).suffix.lstrip('.')
        modifeided_time = os.path.getmtime(scanning_path)
        modifeided_date = datetime.datetime.fromtimestamp(modifeided_time).strftime("%d-%m-%Y %I:%M %p") 
        sizes = f"{Path(scanning_path).stat().st_size} Bytes"
        # data = [names_types[0], sizes, names_types[1], modifeided_date]
        data = [file_name, sizes, file_ext, modifeided_date]
        with open(npath, 'a', encoding="utf-8", newline='') as f:
            writ = csv.writer(f)
            writ.writerow(data)
        
def backup_archive():
    report_saving_csv()
    t1 = time.time()
    try:
        print("📦 Backuping...")
        shutil.make_archive(str(backup_folder), 'zip', scan_path)
        print(f"✅ Backup succeeded: {backup_folder}.zip")
    except Exception as e:
        print(f"❌ Failed to backup: {e}")
    t2 = time.time()
    print(f"⏱️ Backup took: {round(t2 - t1, 2)} seconds.")

backup_archive()

# bb = Path(filename).mkdir(parents=True, exist_ok=True)
# print(bb)
# print(root)
# print(scanning_path)
# print(scanned)

# 🧠 Features:
# ✅ Folder chooser via command-line or default folder

# 📂 फोल्डर के अंदर की सभी files scan करो

# 🧾 CSV/JSON रिपोर्ट बनाओ (name, size, type, last modified)

# 💾 बैकअप copy बनाओ (with date-time folder)

# 🕒 कितना time लगा - show करो

# 🧠 Bonus: Pickle से पिछली स्कैनिंग सेव करके compare करो

# 📁 Scanning folder: /home/user/Documents
# 📄 12 files found.
# ✅ Report saved to: report_2025-05-15.csv
# ✅ JSON report saved: report_2025-05-15.json
# 📦 Backup created: backup_2025-05-15_143522/
# 🕒 Process completed in 2.56 seconds

# import shutil, datetime, time
# from pathlib import Path

# scan_path = r"E:\BIJAY\python\PYTHON\Moduel"
# backup_path = r"E:\BIJAY\python\PYTHON\Moduel\MATH"
# filename = f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
# backup_folder = Path(backup_path) / filename

# def report_saving_csv():
#     # Dummy function (actual CSV report logic yahan aayega)
#     print("Report saved before backup...")

# def backup_archive():
#     report_saving_csv()
#     t1 = time.time()
#     try:
#         print("📦 Backuping...")
#         shutil.make_archive(str(backup_folder), 'zip', scan_path)
#         print(f"✅ Backup succeeded: {backup_folder}.zip")
#     except Exception as e:
#         print(f"❌ Failed to backup: {e}")
#     t2 = time.time()
#     print(f"⏱️ Backup took: {round(t2 - t1, 2)} seconds.")

# # Run the function
# backup_archive()
