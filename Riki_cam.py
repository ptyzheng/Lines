import cv2
import numpy as np

friends = cv2.VideoCapture(1)

while True:
    ret,frame = friends.read()
    cv2.imshow('friend_display', frame)
    if cv2.waitKey(1) & 0xFF==ord('c'):
        frame = np.transpose(frame)
        cv2.imwrite('face.png', frame)
    if cv2.waitKey(100) & 0xFF==ord('q'):
        break

 
cv2.VideoCapture.release(friends)
cv2.destroyAllWindows()
