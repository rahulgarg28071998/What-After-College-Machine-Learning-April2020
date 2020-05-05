import numpy as np
import cv2
import os

cap = cv2.VideoCapture(0)

# Face Detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")


# Testing 

while True:
	ret,frame = cap.read()
	if ret == False:
		continue

	faces = face_cascade.detectMultiScale(frame,1.3,5)
	if(len(faces)==0):
		continue

	for face in faces:
		x,y,w,h = face

		#Get the face ROI
		offset = 10
		face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset]
		face_section = cv2.resize(face_section,(100,100))



	key = cv2.waitKey(1) & 0xFF
	if key==ord('q'):
		break

cap.release()
cv2.destroyAllWindows()