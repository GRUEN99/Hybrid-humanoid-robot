

import cv2
import face_recognition
import pickle
import os

PATH_FOR_USER_IAMGES = r"C:\Users\M\PycharmProjects\pythonProject2\dependencies\user_images"
IMAGES = os.listdir(PATH_FOR_USER_IAMGES)
PATHS_FOR_ALL_IAMGES = [os.path.join(PATH_FOR_USER_IAMGES ,imagename) for imagename in IMAGES]

def trainModel(PATHS_FOR_ALL_IAMGES , IMAGES):
    knownEncodings = []
    knownNames = []
    # loop over the image paths
    for (index, imagePath) in enumerate(PATHS_FOR_ALL_IAMGES):
        try:
            image = cv2.imread(imagePath)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            #Use Face_recognition to locate faces
            boxes = face_recognition.face_locations(rgb)
            # compute the facial embedding for the face
            encodings = face_recognition.face_encodings(rgb, boxes)
            # loop over the encodings
            for encoding in encodings:
                knownEncodings.append(encoding)
                knownNames.append(IMAGES[index][:-4])
            print('model trained for ',IMAGES[index])
        except:
            continue
    #save emcodings along with their names in dictionary data
    data = {"encodings": knownEncodings, "names": knownNames}
    #use pickle to save data into a file for later use
    faceEncodingsFile = open(r"C:\Users\M\PycharmProjects\pythonProject2\dependencies\face_enc", "wb")
    faceEncodingsFile.write(pickle.dumps(data))
    faceEncodingsFile.close()
    print('Training completed')
    return

if __name__=="__main__":
    trainModel(PATHS_FOR_ALL_IAMGES, IMAGES)
    
        
        