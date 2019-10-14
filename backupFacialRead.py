import cv2
import sys


# draws label 
def __draw_label(img, text, pos, bg_color):
    font_face = cv2.FONT_HERSHEY_SIMPLEX
    scale = 0.4
    color = (0, 0, 0)
    thickness = cv2.FILLED
    margin = 6

    txt_size = cv2.getTextSize(text, font_face, scale, thickness)

    end_x = pos[0] + txt_size[0][0] + margin
    end_y = pos[1] - txt_size[0][1] - margin

    cv2.rectangle(img, pos, (end_x, end_y), bg_color, thickness)
    cv2.putText(img, text, pos, font_face, scale, color, 1, cv2.LINE_AA)


cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
video_cap2 = cv2.VideoCapture(1)
video_feed = [video_capture, video_cap2]
video_names = ['cam1', 'cam2']

frames = [None] * 2;
gray = [None] * 2;
ret = [None] * 2;

while True:
    # Capture frame-by-frame
    for i, c in enumerate(video_feed):
        if c is not None:
            ret[i], frames[i] = c.read();
    for i,f in enumerate(frames):
        if ret[i] is True:
            gray[i] = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
            if(i == 0):
                faces = faceCascade.detectMultiScale(
                    gray[i],
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags= cv2.CASCADE_SCALE_IMAGE
                )
                # Draw a rectangle around the faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(frames[i], (x, y), (x+w, y+h), (0, 255, 0), 2)

                #display count frame
                __draw_label(frames[i], "No. People: {0}".format(len(faces)), (20,20), (255,255,255))
            # Display the resulting frame
            cv2.imshow(video_names[i],frames[i]);

    #cv2.imshow('Video', frame)

    # Display the resulting frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()