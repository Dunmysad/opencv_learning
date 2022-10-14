import numpy as np

import cv2 as cv


haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['zgr', 'lm', 'ljj', 'zjl', 'dzq']

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\li\Desktop\opencv_learning\faces\dzq\12.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)

faces_rect = haar_cascade.detectMultiScale(gray)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(people[label], confidence)

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv.imshow('face', img)
cv.waitKey(0)