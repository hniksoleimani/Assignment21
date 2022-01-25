import cv2
img=cv2.imread("img.jpg",0)
print(img.shape)
threshold=150
height,width=img.shape
for i in range(height):
    for j in range(width):
        if img[i,j] <threshold:
            img[i,j]=0
cv2.imwrite("wolf.jpg",img)
cv2.imshow("Anything",img)
cv2.waitKey()


