import cv2 as cv
import numpy as np
img = cv.imread(r"C:\Users\salwa\Downloads\371533082_1048648173174637_3384000278143686871_n.jpg")
  #Averaging ( filtre moyenneur )
average = cv.blur(img, (7,7))
cv.imshow('average',average)
  #Gausian blur (each index has a weight)
gauss = cv.GaussianBlur(img , (7,7), 0)
cv.imshow("gausian blur", gauss)
  #Median Blur ( filtre médiane ) ( salt and pepper noise)
median = cv.medianBlur(img,7)
cv.imshow("median blur", median)
 # Bilateral blur
bil = cv.bilateralFilter(img,5, 15, 15)
cv.imshow("bil blur", bil)
cv.waitKey(0)