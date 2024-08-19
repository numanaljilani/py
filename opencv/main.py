import cv2


# img = cv2.imread('taj.jpg',0)
img = cv2.imread('taj.jpg')

# roi = img[100:160 , 90:120]


# resize = cv2.resize(img ,(400,350)) #RESIZE IMAGE 
# imge2 = cv2.rotate(img,cv2.ROTATE_180) # ROTATE IMAGE

img = cv2.putText(img , text="This is a open cv" ,org=(500 , 500) , fontFace=cv2.FONT_HERSHEY_DUPLEX , color=(255,0,0) , thickness=5,fontScale=2)
img = cv2.rectangle(img , (100,200),(220 , 321),(0,0,255) , thickness=10)
img = cv2.circle(img , (300,500) , 100 , (0,255,0) , 5)
cv2.imwrite("text.png",img)
cv2.imshow("Image",img)

cv2.waitKey(0)
