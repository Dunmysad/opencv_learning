import cv2 as cv
from cv2 import minEnclosingCircle
from matplotlib.scale import scale_factory

img = cv.imread('photos/group2.jpg')
cv.imshow('Lady', img)

# 灰度
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray)

print(len(faces_rect))

# 识别多个加框
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)
cv.waitKey(0)