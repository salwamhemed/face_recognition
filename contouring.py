import cv2 as cv
import numpy as np
img = cv.imread(r"C:\Users\salwa\Downloads\371533082_1048648173174637_3384000278143686871_n.jpg")
img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# blur= cv.GaussianBlur(img2 , (5,5), cv.BORDER_DEFAULT)
# canny = cv.Canny(blur,125,175)
# cv.imshow("canny",canny)
# contours , hie = cv.findContours(canny , cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)}')
ret , thresh = cv.threshold(img2 , 125 , 255,cv.THRESH_BINARY)
contours , hie = cv.findContours(thresh , cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)}')
cv.imshow("thresh", thresh)


blank = np.zeros(img.shape,dtype='uint8')
cv.imshow("blank",blank)
cv.drawContours(blank,contours , -1 , (0,0,255),1)
cv.imshow("shape", blank)
cv.waitKey(0)