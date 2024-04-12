import cv2, os
import numpy as np
from PIL import Image

path="C:/Users/Juan/Documents/openCV/lesson 6/images"

os.chdir(path)

numFiles=len(os.listdir("."))
print(numFiles)


mean_w=0
mean_h=0


for images in os.listdir('.'):
    img=Image.open(os.path.join(path,images))
    w,h=img.size
    mean_w+=w
    mean_h+=h

mean_h=mean_h//numFiles
mean_w=mean_w//numFiles


for images in os.listdir('.'):
    img=Image.open(os.path.join(path,images))
    imgResize=img.resize((mean_w,mean_h), Image.LANCZOS)
    imgResize.save(images,'JPEG',quality=95)


def videoGenerator():
    myvid="myvideo.avi"
    pics=[]

    for images in os.listdir('.'):
        pics.append(images)

    frame=cv2.imread(os.path.join('.',pics[0]))

    h,w,c=frame.shape
    video=cv2.VideoWriter(myvid, 0, 1, (h,w))

    for images in pics:
        video.write(cv2.imread(os.path.join('.',images)))

    video.release()


videoGenerator()

    
