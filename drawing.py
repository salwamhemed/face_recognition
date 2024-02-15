import cv2 as cv
import numpy as np
img = cv.imread(r"C:\Users\salwa\Downloads\371533082_1048648173174637_3384000278143686871_n.jpg")
 #paint the image
blank=np.zeros((500,500,3),dtype='uint8')
blank[250:500,0:250] = 0 ,255 , 0
 #draw a rectangle
rect = cv.rectangle(img , (0,0),(img.shape[1]//2,img.shape[0]//2),(0,0,255 ) , thickness= cv.FILLED)
 #draw a circle
circle = cv.circle(img,(img.shape[1]//2,img.shape[0]//2),50,(0,255,0),thickness=-1)
 #draw a line
line = cv.line(img , (0,0),(250,250),(255,255,255),thickness=3)
cv.imshow('blank',rect)
 #write a text
text = cv.putText(blank , 'hello' , (255,255), cv.FONT_HERSHEY_TRIPLEX , 1.0 , (255 , 0 , 0 ),thickness=2)
cv.imshow('text',blank)
cv.waitKey(0)