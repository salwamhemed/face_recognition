import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread(r"C:\Users\salwa\Downloads\371533082_1048648173174637_3384000278143686871_n.jpg")
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

#Laplaciian 
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian",lap)
#Sobel 
sobelx = cv.Sobel(gray, cv.CV_64F, 1 , 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0 , 1)
combined = cv.bitwise_and(sobelx,sobely)
cv.imshow("combined ", combined)
#Canny
canny = cv.Canny(gray, 150 , 175)
cv.imshow("canny",canny)

cv.waitKey(0)  