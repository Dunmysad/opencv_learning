import cv2 as cv

img = cv.imread('photos/1.jpg')
cv.imshow('ph', img)



# 平均
average = cv.blur(img, (8,8))
cv.imshow('Average Blur', average)

# 高斯模糊
gauss = cv.GaussianBlur(img, (7,7),0)
cv.imshow('Gauss', gauss)


# 中值模糊
median = cv.medianBlur(img, 5)
cv.imshow('Median', median)

# Bilateral
# 双边模糊
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bil', bilateral)



cv.waitKey(0)