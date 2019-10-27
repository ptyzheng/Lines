import cv2
import os
import sys
import numpy as np
import face_recognition

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


def face_loader(path):
    return known_face_names, known_face_encodings

path = './faces/'
known_face_names = []
known_face_encodings = []

known_face_names, known_face_encodings = face_loader(path)

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

#premade cascade from Intel that does facial detection
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

#cameras 1, 2
video_capture = cv2.VideoCapture(0)
video_feed = [video_capture]
video_names = ['cam1']

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
            
            faces = faceCascade.detectMultiScale(
                gray[i],
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags= cv2.CASCADE_SCALE_IMAGE
            )
                # Draw a rectangle around the faces
            

            if i == 0:
                small_frame = cv2.resize(frames[i], (0, 0), fx=0.25, fy=0.25)

                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_small_frame = small_frame[:, :, ::-1]
                if process_this_frame:
                    # Find all the faces and face encodings in the current frame of video
                    face_locations = face_recognition.face_locations(rgb_small_frame)
                    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                    face_names = []
                    for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                        name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                        best_match_index = np.argmin(face_distances)
                        if matches[best_match_index]:
                            name = known_face_names[best_match_index]

                        face_names.append(name)

                process_this_frame = not process_this_frame
    			# Display the results
                for (top, right, bottom, left), name in zip(face_locations, face_names):
        			# Scale back up face locations since the frame we detected in was scaled to 1/4 size
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

        			# Draw a box around the face
                    cv2.rectangle(frames[i], (left, top), (right, bottom), (0, 0, 255), 2)

        			# Draw a label with a name below the face
                    cv2.rectangle(frames[i], (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frames[i], name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting frames
            cv2.imshow(video_names[i],frames[i]);

    #if q pressed, terminate
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()