import cv2 as cv
import numpy as np
img = cv.imread(r"C:\Users\salwa\Downloads\371533082_1048648173174637_3384000278143686871_n.jpg")
cv.imshow("salwa",img)
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1 , minNeighbors=7)
print(f'number of faces = {len(faces_rect)}')
for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+w),(0,255,0),thickness=2)
cv.imshow("detected faces",img)
cv.waitKey(0)