
import cv2 as cv

img = cv.imread('./photos/1.jpg')

cv.imshow('cat', img)

# 灰度
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# 模糊
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# 边缘级联
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# 主导图像 
# Dilate the image
dilate = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilate', dilate)

# Eroding
eroded = cv.erode(dilate, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

cv.waitKey(0)