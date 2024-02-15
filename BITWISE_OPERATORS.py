import cv2 as cv
import numpy as np
img = cv.imread(r"C:\Users\salwa\Downloads\371533082_1048648173174637_3384000278143686871_n.jpg")

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255, -1 )
circle = cv.circle(blank.copy(),(200,200),200,255,-1)
 # BITWISE AND
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow("bit and", bitwise_and)
# BITWISE OR
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("bit or", bitwise_or)
# BITWISE XOR
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("bit xor", bitwise_xor)
# BITWISE NOT
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("bit not", bitwise_not)
cv.imshow("rectangle",rectangle)
cv.imshow("cercle",circle)
cv.waitKey(0)