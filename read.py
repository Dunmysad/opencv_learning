import cv2 as cv

# img = cv.imread('./photos/wallhaven-rdv22j.jpg')

# cv.imshow('cat', img)


capture = cv.VideoCapture('video/1.mp4')


while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()
