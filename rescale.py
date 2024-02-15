import cv2 as cv
img = cv.imread(r"C:\Users\salwa\Downloads\A P P S.png")
cv.imshow('salwa',img)

def rescaleFrame(frame,scale=0.2):
    width= int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
salwa2 = rescaleFrame(img)
cv.imshow('salwa2',salwa2)
vid = cv.VideoCapture(r"C:\Users\salwa\Downloads\Cardigan - Taylor Swift  edit audio .mp4")
while True :
    isTrue , frame = vid.read()
    newFrame= rescaleFrame(frame)
    cv.imshow('cardigan',frame)
    cv.imshow('cardigan2',newFrame)
    if cv.waitKey(10) & 0xFF==ord('d') :
        break
vid.release()

cv.waitKey(0)