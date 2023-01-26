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
    while not_taken:
        try:
            with open(img_path,'r') as f:
                not_taken=False
                extract(img_path)
        except:
            time.sleep(0.5)


def extract(img_path):

    # extract text from screenshot
    text=pytesseract.image_to_string(PIL.Image.open(img_path))
    print(text)

    # delete the taken screenshot 
    de = f"rm {img_path}"
    subprocess.run(de,shell=True,check=True)


if __name__ =="__main__":
    # get the path of current dir and check whether temp dir created or not

    path=pathlib.Path(__file__).parent.resolve()
    temp=pathlib.Path(f"{path}/temp")

    if not temp.is_dir():
        temp.mkdir(parents=True,exist_ok=True)  # if not created , create temp dir

    # path for screenshot img
    img_path=f"{temp}/out.png"
  
    takeScreenshot(img_path)
