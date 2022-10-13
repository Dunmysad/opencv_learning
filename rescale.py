
from turtle import width
import cv2 as cv
from cv2 import resize

img = cv.imread('./photos/1.jpg')

cv.imshow('cat', img)

# 缩放算法
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensons = (width, height)
    return cv.resize(frame, dimensons, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('video/1.mp4')


resized_image = rescaleFrame(img)
cv.imshow('image', resized_image)

# 改变实时视频
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('video',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()
