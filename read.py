import cv2 as cv
img = cv.imread(r"C:\Users\salwa\Downloads\A P P S.png")
cv.imshow('salwa',img)
vid = cv.VideoCapture("C:\Users\salwa\Downloads\_Saltburn_ Made Me Physically Sick.mp4")
while True :
    isTrue , frame = vid.read()
    cv.imshow('cardigan',frame)
    if cv.waitKey(10) & 0xFF==ord('d') :
        break
vid.release()
cv.destroyAllWindows()
cv.waitKey(0)