import cv2
img=cv2.imread("/home/ali/hani/Learning/Session21/Assignment 21/1.jpg",0)
print(img)
print(img.shape)
img_r=(255-img)
cv2.imwrite("Output.jpg",img_r)

