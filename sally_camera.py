import cv2
import numpy as numpy

camera = cv2.VideoCapture(0)
while True:
    ret,frame = camera.read()
    cv2.imshow('camera', frame) 
    if cv2.waitKey(1) & 0xFF == ord('c'):
        userFile = input("What do you want to call your file?")
        fileName = 'sally-camera/' + userFile + '.png'
        cv2.imwrite(fileName,frame)
    if cv2.waitKey(100) & 0xFF == ord('z'):
        break
    if cv2.waitKey(200) & 0xFF == ord('p'):
        print("PRINTED")
camera.release()
cv2.destroyAllWindows()