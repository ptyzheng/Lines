import cv2
import numpy as np

# Capture webcam footage
cam = cv2.VideoCapture(0);

# Booleans for toggling
gscale = False
transposed = False

while(True):
    # Read frame of camera
    ret, frame = cam.read()

    # If statements to manipulate video output
    if gscale:
        # Convert frame to grayscale and display
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Window 1', gray)
    else:
        if transposed:
            # Convert frame to grayscape, transpose it 90 degrees
            # counterclockwise, then display
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = np.transpose(gray)
            cv2.imshow('Window 1', gray)
        else:
            # Display frame normally
            cv2.imshow('Window 1', frame)

    # Read keyboard input
    if cv2.waitKey(1) & 0xFF == ord('q'):
        name = input("Enter file name: ")
        cv2.imwrite(name + ".png", frame)
    if cv2.waitKey(1) & 0xFF == ord('f'):
        toggle = not toggle
    if cv2.waitKey(1) & 0xFF == ord('p'):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = np.transpose(gray)
        cv2.imshow("rotate.png", gray)
    if cv2.waitKey(1) & 0xFF == ord('t'):
        transposed = not transposed
    if cv2.waitKey(1) & 0xFF == ord('z'):
        break

cam.release()
cv2.destroyAllWindows()
