#  import necessary libraries  

import pytesseract  # contact tesseract ocr
import PIL.Image    # pillow to interact with image
import subprocess   # to run bash command
import time         # time to wait 
import pathlib      # dealing with paths



def takeScreenshot(img_path):
    # take screenshot
    cmd=f"spectacle -bro{img_path}"
    res=subprocess.run(cmd,shell=True,check=True)
    not_taken=True
    img_path=pathlib.Path(img_path)
    while not_taken:
        try:
            if img_path.exists():
                not_taken=False
                return True
        except:
            time.sleep(0)


def extract(img_path,la="eng"):
    # extract text from screenshot
    text=pytesseract.image_to_string(PIL.Image.open(img_path),lang=la)
    print(text)

    # delete the taken screenshot 
    de = f"rm {img_path}"
    subprocess.run(de,shell=True,check=True)

def chooseLang():
    cmd="tesseract  --list-langs"
    res=subprocess.run(cmd,shell=True,stdout=subprocess.PIPE,check=True)
    langs=res.stdout.decode('UTF-8').splitlines()[1:]
    while True:
        for i,lang in enumerate(langs):
            print(f"{i+1}  {lang} ")
        try:
            lang=int(input("Choose the lang : "))
        except:
            print("choose correct lang ")
            continue
        if lang <0 or lang > len(langs):
            continue
        else:
            break
    return langs[lang-1]

    

if __name__ =="__main__":
    # get the path of current dir and check whether temp dir created or not

    path=pathlib.Path(__file__).parent.resolve()
    temp=pathlib.Path(f"{path}/temp")

    if not temp.is_dir():
        temp.mkdir(parents=True,exist_ok=True)  # if not created , create temp dir

    # path for screenshot img
    img_path=pathlib.Path(f"{temp}/out.png")
  
    # takeScreenshot(img_path)
    print("Choose the lang you are going to Extract By selecting its number: ")
    lang=chooseLang()
    print(f"You choosen {lang} lang")
    takeScreenshot(img_path)
    extract(img_path,lang)

