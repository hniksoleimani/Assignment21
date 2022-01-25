import cv2
import numpy as np


#-------------------------------------------------------------------------------------
def flip(imgg):
    img_r=np.zeros([1057,1920,3], np.uint8)
    for i in range (height):
        img_r[i,:]=img[1057-i-1,:]
    return(img_r)

#-------------------------------------------------------------------------------------

img=cv2.imread("/home/ali/hani/Learning/Session21/Assignment 21/3.jpg")
print(img.shape)
height,width,depth=img.shape
print(height)
varr=flip(img)

#-------------------------------------------------------------------------------------

cv2.imwrite("/home/ali/hani/Learning/Session21/Answers/3.jpg",varr)