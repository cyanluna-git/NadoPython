from PIL import Image
from pytesseract import *
import cv2
import os

def Conversion(file):
    multiple = 4
    image = cv2.resize(cv2.imread(file),(0,0),fx=multiple, fy=multiple, interpolation=cv2.INTER_LINEAR)
    text = image_to_string(image,lang="eng",config='--psm 1 -c preserve_interword_spaces=1')
    return text

def ParseText(text, cnt_row, cnt_col):
    text = text.replace('\n\n','\n')
    list = text.split('\n') 
    list.remove("")
    result=[]
    for i in range(cnt_row):
        temp=[]
        for j in range(cnt_col):
            temp.append(list[i + j*cnt_row])
        result.append(temp)
    return result
    


if __name__ == '__main__':
    # Current directory
    this_program_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(this_program_directory)

    # Set environment variable path
    tesseract_home = "C:\\Program Files\\Tesseract-OCR"
    if tesseract_home not in os.environ["PATH"].split(os.pathsep):
        os.environ["PATH"] += os.pathsep + tesseract_home

    # Read config file
    config = f'{this_program_directory}\\Path_Capture_Folder.ini'
    with open(config,'r') as f:
        folder = f.readline() # 사진파일 저장 폴더, Config.ini 내부에서 지정
        f.close
    fileext = ('.jpg','.JPG','.png','.PNG')
    photos = [os.path.join(folder,file) for file in os.listdir(folder) if file.endswith(fileext)]
    
    for photo in photos:
        print('Converting "{}" in progress...'.format(os.path.basename(photo)))
        result_file = os.path.splitext(photo)[0] + '.csv'
        result = ParseText(Conversion(photo),5,4)
        r = open(result_file,'w')
        for row in result:
            string = ",".join(row)
            r.write(string + '\n')
        r.close
    
    input('Press Enter to Finish.')




