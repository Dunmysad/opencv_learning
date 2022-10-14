import re
import cv2 as cv
import numpy as np


img = cv.imread('photos/1.jpg')
cv.imshow('img', img)


blank = np.zeros(img.shape[:2], dtype='uint8')


# 通道分割
b,g,r = cv.split(img)


blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])


cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)


print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


# 合并通道
merged = cv.merge([b,g,r])
cv.imshow('Merged image', merged)


cv.waitKey(0)