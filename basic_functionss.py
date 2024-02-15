import cv2 as cv
img = cv.imread(r"C:\Users\salwa\Downloads\371533082_1048648173174637_3384000278143686871_n.jpg")
img2 = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow("image",img)
cv.imshow("image2",img2)
 #blur
blurimg = cv.GaussianBlur(img , (7,7) , cv.BORDER_DEFAULT)
cv.imshow("blur",blurimg)
 #canny_edges
canny = cv.Canny(img , 0 , 500)
cv.imshow("canny",canny)
 #dilatating
dilated = cv.dilate(canny , (3,3), iterations=1)
cv.imshow("dilated",dilated)
 #Resize/cropping
resized = cv.resize(img , (500,500))
cv.imshow("resized",resized)
cropped = img[50:200 , 60:300]
cv.imshow("cropped",cropped)
cv.waitKey(0)