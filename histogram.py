import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread(r"C:\Users\salwa\Downloads\371533082_1048648173174637_3384000278143686871_n.jpg")
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank, (img.shape[1]//2 , img.shape[0]//2),150,255,-1)
mask = cv.bitwise_and(img , img , mask=circle)

cv.imshow("mask", mask)

#gray_hist = cv.calcHist([gray],[0],mask, [256], [0,256])
"""
plt.figure()
plt.title('grayscale histogram')
plt.xlabel('bins')
plt.ylabel('nb of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
# color histogram 
"""
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist, color=col)
plt.show()  
cv.waitKey(0)