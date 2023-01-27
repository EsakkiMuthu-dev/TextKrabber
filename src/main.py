#  import necessary libraries  

import pytesseract  # contact tesseract ocr
import PIL.Image    # pillow to interact with image
import subprocess   # to run bash command
import time         # time to wait 
import pathlib      # dealing with paths
from pyperclip import copy     # for clipboard management

# for GUI
from PyQt5.QtWidgets import *
from PyQt5 import uic







# def chooseLang():
#     cmd="tesseract  --list-langs"
#     res=subprocess.run(cmd,shell=True,stdout=subprocess.PIPE,check=True)
#     langs=res.stdout.decode('UTF-8').splitlines()[1:]
#     while True:
#         for i,lang in enumerate(langs):
#             print(f"{i+1}  {lang} ")
#         try:
#             lang=int(input("Choose the lang : "))
#         except:
#             print("choose correct lang ")
#             continue
#         if lang <0 or lang > len(langs):
#             continue
#         else:
#             break
#     return langs[lang-1]


# Gui
class gui(QMainWindow):
    def __init__(self) -> None:
        super(gui,self).__init__()
        uic.loadUi("/home/peace/Documents/TextKrabber/src/UI/TextKrabber.ui",self)
        self.show()
        # langs
        self.generateLangOptions()
        self.lang="eng"
        self.langs.currentIndexChanged.connect(lambda : self.chooseLang() )
        self.about.triggered.connect(lambda:self.aboutMe())
        self.addLanguage.triggered.connect(lambda:self.installLang())
        imgPath=self.generatepath()
        self.grap.clicked.connect(lambda:self.takeScreenshot(imgPath))
        self.actionClose.triggered.connect(exit)
    
    def aboutMe(self):
        msg=QMessageBox()
        msg.setWindowTitle("About")
        msg.setText("\n \t Text Krabber \t  \n \n ")
        msg.exec_()
        

    def generateLangOptions(self):
        cmd="tesseract  --list-langs"
        res=subprocess.run(cmd,shell=True,stdout=subprocess.PIPE,check=True)
        ls=res.stdout.decode('UTF-8').splitlines()[1:]
        ls.remove("osd")
        self.langs.addItems(ls)

    def installLang(self):
        msg=QMessageBox()
        msg.setWindowTitle("Add Languages")
        msg.setText("\n You Can install Additional Languages by using this command :- \n \n \"sudo <ur package manger> install tesseract ocr-<ocr lang code>\". \n \n Find your language code in  https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html")
        msg.exec_()
    def chooseLang(self):
        self.lang=self.langs.currentText()

    def generatepath(self):
        # get the path of current dir and check whether temp dir created or not
        path=pathlib.Path(__file__).parent.resolve()
        temp=pathlib.Path(f"{path}/temp")

        if not temp.is_dir():
            temp.mkdir(parents=True,exist_ok=True)  # if not created , create temp dir

        # path for screenshot img
        img_path=pathlib.Path(f"{temp}/out.png")
        return img_path

    def takeScreenshot(self,imgPath):
        self.showMinimized()
        # take screenshot
        cmd=f"spectacle -bro{imgPath}"
        res=subprocess.run(cmd,shell=True,check=True)
        not_taken=True
        imgPath=pathlib.Path(imgPath)
        while not_taken:
            try:
                if imgPath.exists():
                    not_taken=False
            except:
                time.sleep(0)
        
        self.extract(imgPath,self.lang)
    

    def extract(self,imgPath,la="eng"):
        # extract text from screenshot
        text=pytesseract.image_to_string(PIL.Image.open(imgPath),lang=la)
        copy(text)

        self.showNormal()
        # delete the taken screenshot 
        de = f"rm {imgPath}"
        subprocess.run(de,shell=True,check=True)
        self.finishMsg.setText("Check out Your Clipboard!📎")
        self.grap.setText("Take another shot")
        

if __name__ =="__main__":

  
    # takeScreenshot(img_path)
    # print("Choose the lang you are going to Extract By selecting its number: ")
    # lang=chooseLang()
    # print(f"You choosen {lang} lang")
    # takeScreenshot(img_path)
    # extract(img_path,lang)

    app=QApplication([])
    window=gui()
    app.exec_()


