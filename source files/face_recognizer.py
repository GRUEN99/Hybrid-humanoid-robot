import cv2
import face_recognition
import pickle
import os
from PIL import Image, ImageDraw
#import config
import numpy as np

class FaceRecognizer:
    def __init__(self):
        self.VISUALS = cv2.VideoCapture(0)
        self.data = pickle.loads(open(r'/home/Desktop/dependencies/face_enc', "rb").read())


    def recognizeFaces(self ,image , visualize = False):

        faceLocations = face_recognition.face_locations(image)
        faceEncodings = face_recognition.face_encodings(image, faceLocations)
        # Convert to PIL format
        pilImage = Image.fromarray(image)
        knownFaceEncodings = self.data.get('encodings')
        knownFaceNames = self.data.get('names')
        # Create a ImageDraw instance
        draw = ImageDraw.Draw(pilImage)
        names = []
        # Loop through faces in test image
        faceIndex = 0
        for(top, right, bottom, left), faceEncoding in zip(faceLocations, faceEncodings):
            matches = face_recognition.compare_faces(knownFaceEncodings, faceEncoding , tolerance = 0.45)
            name = "Unknown"
            # If match
            if True in matches:
                firstMatchIndex = matches.index(True)
                name = knownFaceNames[firstMatchIndex]

                # Draw box
                draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))
                # Draw label
                textWidth, textHeight = draw.textsize(name)
                draw.rectangle(((left,bottom - textHeight - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
                draw.text((left + 6, bottom - textHeight - 5), name, fill=(0,0,0))
            else:
                draw.rectangle(((left, top), (right, bottom)), outline=(0,255,0))
                faceIndex += 1
                # Draw label
                textWidth, textHeight = draw.textsize(name)
                draw.rectangle(((left,bottom - textHeight - 20), (right, bottom)), fill=(0,255,0), outline=(0,255,0))
                draw.text((left + 6, bottom - textHeight - 15), 'new user', fill=(0,0,0))

            names.append(name)
        del draw

        if(visualize):
            testImage = np.array(pilImage)
            return names , testImage
        return names
