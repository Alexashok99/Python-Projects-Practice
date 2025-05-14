
import os
import sys
import shutil

class FileOrganizer:
    def __init__(self):       
        self.dict_ext = {'Image':['.jpg','.jpeg','.png','.svg'],
                         'Python': ['.py'],
                         'Text': ['.txt'],
                         'Videos': ['.mp4', '.avi','.mov','.gif'],
                         'Audio': ['.mp3','.wav','.flac'],
                         'Document': ['.pdf', '.doc','.docx', '.xlsx','.xls','.csv','.json','.js'],
                         'Compressed': ['.zip','.rar'],
                         'Others': []

                        }
        
        self.argu = sys.argv[1]

        self.file_dir()

    # inp = "E:\\BIJAY\\python\\PYTHON\\Moduel\\OS_MODULE"
    def file_dir(self):
        # inp = input("Enter Folder Location: ")
        file_list = os.listdir(self.argu)
        for files in file_list:
            files_extn = os.path.splitext(files)[1]
            # print(files_extn)
            for key , value in self.dict_ext.items():
                if os.path.exists(key)==0:
                    os.makedirs(self.argu, key)
                # print(key)
                for ext in value:
                    # print(ext)
                    if files_extn==ext:
                        # print("Match")
                        shutil.copy(files, key)
                    # else:
                        # print("Else")

if __name__ == "__main__":
    FileOrganizer()


# def check():
#     for key , value in self.dict_ext.items():
#         print(key)
#         for ext in value:
#             print(ext)

# file_dir(inp)