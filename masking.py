import cv2 as cv
import numpy as np
img = cv.imread(r"C:\Users\salwa\Downloads\371533082_1048648173174637_3384000278143686871_n.jpg")
blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2 , img.shape[0]//2),150,255,-1)
cv.imshow("mask",mask)

masked = cv.bitwise_and(img , img , mask=mask)
cv.imshow("masked img", masked)
cv.waitKey(0)