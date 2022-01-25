import numpy as np
import cv2

#-------------------------------------------------------------------------------------
def ribbon(imgg):

    new_img=cv2.resize(img,(600,800))
    height,width=new_img.shape
    for i in range(0,height):
        for j in range(400,width):
            if((i-j+400)==0):
                new_img[i,j:j+50]=0
    return(new_img)
        



# for i in range(0,100):
#     for j in range(300,400):
#         if((i-j+300)==0):
#             new_img[i,j:j+100]=0


img=cv2.imread("Picture2.jpg",0)
print(img.shape)
varr=ribbon(img)
#-------------------------------------------------------------------------------------
cv2.imwrite('pic.jpg', varr)

