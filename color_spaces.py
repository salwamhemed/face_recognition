import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread(r"C:\Users\salwa\Downloads\371533082_1048648173174637_3384000278143686871_n.jpg")
cv.imshow('salwa',img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)
rgb = cv.cvtColor (img , cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

hsv = cv.cvtColor(img , cv.COLOR_BGR2HSV)
#cv.imshow('hsv',hsv)

lab = cv.cvtColor(img , cv.COLOR_BGR2LAB)
#cv.imshow('lab',lab)

plt.imshow(rgb)
plt.show()

#cv.waitKey(0)