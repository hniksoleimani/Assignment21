import cv2
import numpy as np

#-------------------------------------------------------------------------------------

def gradient(imgg):
    for i in range (height):
        for j in range(width):
            img_g[i,j]=255
    for i in range(height):       
        row=480-i-1
        k=(row/height)*255
        img_g[i,:]=k
    return(img_g)

#-------------------------------------------------------------------------------------

img_g=np.zeros([480,480], np.uint8)
height,width=img_g.shape
print(img_g.shape)
print(height)
varr=gradient(img_g)

#-------------------------------------------------------------------------------------

cv2.imwrite("/home/ali/hani/Learning/Session21/Answers/4.jpg",varr)