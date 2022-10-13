import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

# cv.imshow('Blank', blank) 

# img = cv.imread('photos/1.jpg')
# cv.imshow('1', img)

# blank[200:300, 300:400] = 0,255,0

# cv.imshow('Green', blank)

# # 矩形
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
# cv.imshow('Rectangle', blank)

# # 圆形
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
# cv.imshow('Circle', blank)

# # 画线
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
# cv.imshow('Line', blank)

# Write text

cv.putText(blank, 'Hello, xiuguo zuzuzuzuzu', (0,255), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)