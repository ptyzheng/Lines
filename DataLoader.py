import cv2
import os
import sys
import numpy as np
import face_recognition

def face_loader(path):
    known_face_names = []
    known_face_encodings = []
    for filename in os.listdir(path):
       if filename.endswith('.jpg'):
           name_to_store = filename[:-4]
           print(name_to_store)
           known_face_names.append(name_to_store)
           face_image = face_recognition.load_image_file("faces/"+filename)
           known_face_encodings.append(face_recognition.face_encodings(face_image)[0])
           #face_recognition.face_encodings(yang_image)[0]
    return known_face_names, known_face_encodings

