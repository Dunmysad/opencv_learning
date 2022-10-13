import cv2 as cv
import numpy as np


img = cv.imread('photos/1.jpg')


cv.imshow('Boston', img)

# Translation
# 平移
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translate = translate(img, 100, 100)
cv.imshow('Translate', translate)


#  Rotation
# 旋转
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    # 定位旋转点到图片中心
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)



# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)


# Flipping 
# 翻转 0 --> 垂直  1 --> 水平
flip = cv.flip(img, 1)
cv.imshow('Flip',flip)

# Cropping
# 裁剪
cropped = img[200:400, 300:400]
cv.imshow('Cropping', cropped)


cv.waitKey(0)