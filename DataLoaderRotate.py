import cv2
import os
import sys
import numpy as np
from scipy import ndimage, misc
import face_recognition

def face_loader_rotate(path):
    known_face_names = []
    known_face_encodings = []
    
    for filename in os.listdir(path):
       if filename.endswith('.jpg'):
           name_to_store = filename[:-4]
           print(name_to_store)
           face_image = face_recognition.load_image_file("faces/"+filename)
           print(face_image.shape)

           face_image_copy = np.copy(face_image) #deepcopy?
           face_image_copy = cv2.cvtColor( face_image_copy, cv2.COLOR_RGB2GRAY )

           #face_recognition.face_encodings(face_image) returns an array of length 0, not null? https://github.com/ageitgey/face_recognition/issues/100
           #how should we check if it detects an encoding, then?
           if len(face_recognition.face_encodings(face_image)) is 0:
               for degree in [45, 135, 225, 315, 90, 180, 270]:
                   face_image_rotate = ndimage.rotate(face_image_copy, degree)
                   print(face_image_rotate.shape)

                   #problems here
                   if len(face_recognition.face_encodings(face_image_rotate)) is not 0:
                       if face_image_rotate.shape[0] is face_image.shape[0] and face_image_rotate.shape[1] is face_image.shape[1]:
                           face_image = face_image_rotate
                           break

           if len(face_recognition.face_encodings(face_image)) is 0:
               print(filename+" is not valid.")
               os.remove("faces/"+filename)
               
           else:
                print(filename+" is valid.")
                known_face_names.append(name_to_store)
                known_face_encodings.append(face_recognition.face_encodings(face_image)[0])
           
               
           #face_recognition.face_encodings(yang_image)[0]
    return known_face_names, known_face_encodings

face_loader_rotate('./faces/')
