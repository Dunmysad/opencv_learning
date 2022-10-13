import cv2 as cv
import numpy as np


img = cv.imread('photos/map.jpg')
cv.imshow('Boston', img)
 

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# 灰度图像
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 模糊
# blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT )

# 轮廓
canny = cv.Canny(img, 125,175)
cv.imshow('Canny', canny)

# Thresh
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))


cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Draw', blank)


cv.waitKey(0)