
import sys
import os
class FileManager:  
    def __init__(self):         
        self.lsts = ["Image", "Folder","Pajama"]
        self.whl = True
        self.controler()

    def folder_creating(self):
        self.lst = []
        inp = input("Enter Folser: ")
        self.lst.append(inp)
        for folders in self.lst:
            if os.path.exists(folders) == 0:
                os.makedirs(folders)
                print(F"Folder <{folders}> Created Successfully")
            else:
                print(F"Folder <{folders}> Exist")

    def file_show(self):
        folder = os.listdir()
        for files in folder:
            print(files)

    def exit(self):
        print("Exiting...")
        self.whl = False
        sys.exit()

    def path_joining(self):
        path = os.path.join("Folder", "data.txt")
        print(f"It is only string: {path}")

    def delet(self):
        inp = input("Enter File name For DELETE: ")
        if os.path.exists:
            os.removedirs(inp)
            print(f"File <{inp}> DELETED Successfully")
        else: print('Fine not Exist !')

    def controler(self):
        while self.whl:
            menu = """
            File Management System
            Press 1 = Exit
            Press 2 = Show Files
            Press 3 = Create Folder
            Press 4 = Joni Path
            Press 5 = Delete Folder
            """
            print(menu)
            inp = input("Enter Option: ")
            print("")
            if inp == "1":
                self.exit()
                # break
            elif inp == "2":
                self.file_show()
            elif inp == "3":
                self.folder_creating()
            elif inp == "4":
                self.path_joining
            elif inp == "5":
                self.delet()
            else : print("Wrong Input Try Again")


obj = FileManager()
