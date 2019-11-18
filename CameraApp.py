import numpy as np
import cv2

#premade cascade from Intel that does facial detection
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    cv2.imshow('cam', frame)
    path = './faces/'
    if cv2.waitKey(1) & 0xFF == ord('z'):
    	name = input("Enter full name: ")
    	name.replace(" ", "_")
    	file_name = path + name + '.jpg'
    	cv2.imwrite( file_name, frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()