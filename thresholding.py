import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread(r"C:\Users\salwa\Downloads\371533082_1048648173174637_3384000278143686871_n.jpg")
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
# thresh = image , thresholhd = 150
threshold , thresh = cv.threshold(gray, 150, 255 , cv.THRESH_BINARY) # > 150 to 255
cv.imshow("binarisation", thresh)
threshold , thresh_inverse = cv.threshold(gray, 150, 255 , cv.THRESH_BINARY_INV) # < 150 to 255
cv.imshow("binarisation2", thresh_inverse)

# Adaptive thresholding 
adaptive_thresh = cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY , 11 , 3) 
cv.imshow("binarisation2", adaptive_thresh)

cv.waitKey(0)