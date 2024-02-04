import cv2
import numpy as np

class ObjectDetector:
    def __init__(self):
        # yolov3 model will be stored in the 3 files  1 for model architecture (.cfg) , model weights (.weights) , names of the objects it can detect )
        self.model = cv2.dnn.readNet(r'/home/Desktop/dependencies/yolov3.weights',
                                r'/home/Desktop/dependencies/yolov3.cfg')
        with open(r'/home/Desktop/dependencies/coco.names', 'r') as names:
            # class means the class of object
            self.classes = [line.strip() for line in names.readlines()]
            #print(classes)


    def getResults(self , results, image):
        # getting the shape of the image , third parameter is nbr of channels (3) , which we dont need.
        imageHeight, imageWidth, _ = image.shape
        # empty lists to store the details of the detected objects
        classIDs = []
        confidences = []
        boxes = []
        # for each resut in results
        for result in results:
            # one detection consists of coordinates of object in the image(0-1 -- normalized) ,classID , confidence
            for detection in result:
                scores = detection[5:]
                # argmax will give the index of maximum element in the array
                classID = np.argmax(scores)
                confidence = scores[classID]
                if confidence > 0.5:
                    # converting the image coordinates in the range 0-1 to proper pixe coordintes
                    xCoordinateOfCentre = int(detection[0] * imageWidth)
                    yCoordinateOfCentre = int(detection[1] * imageHeight)
                    widthOfDetectedObject = int(detection[2] * imageWidth)
                    heightOfDetectedObject = int(detection[3] * imageHeight)
                    xCoordinateOfDetectedObject = int(xCoordinateOfCentre - widthOfDetectedObject / 2)
                    yCoordinateOfDetectedObject = int(yCoordinateOfCentre - heightOfDetectedObject / 2)
                    # adding the results into the corresponding lists created before
                    boxes.append([xCoordinateOfDetectedObject, yCoordinateOfDetectedObject, widthOfDetectedObject,
                                  heightOfDetectedObject])
                    confidences.append(float(confidence))
                    classIDs.append(classID)
        return classIDs, confidences, boxes


    def drawResults(self,image, classIDs, confidences, boxes):
        # each object can be detected multiple times , to remove the extra detections
        # https://learnopencv.com/non-maximum-suppression-theory-and-implementation-in-pytorch/#:~:text=Non%20Maximum%20Suppression%20%28NMS%29%20is%20a%20technique%20used,selection%20criteria%20to%20arrive%20at%20the%20desired%20results.
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.6)
        font = cv2.FONT_HERSHEY_SIMPLEX
        for boxIndex in range(len(boxes)):
            if boxIndex in indexes:
                xCoordinateOfDetectedObject, yCoordinateOfDetectedObject, widthOfDetectedObject, heightOfDetectedObject = \
                boxes[boxIndex]
                label = str(self.classes[classIDs[boxIndex]])
                # drawing rectangle and labelling the image
                cv2.rectangle(image, (xCoordinateOfDetectedObject, yCoordinateOfDetectedObject), (
                xCoordinateOfDetectedObject + widthOfDetectedObject, yCoordinateOfDetectedObject + heightOfDetectedObject),
                              (0, 255, 0), 2)
                cv2.putText(image, label, (xCoordinateOfDetectedObject, yCoordinateOfDetectedObject + 30), font, 1,
                            (0, 0, 255), 2)
        return


    def detectObjects(self , image):
        # reading the image
        # getting all the layer names in yolov3 model
        layerNames = self.model.getLayerNames()
        # getting output layers from the above list
        outputLayers = [layerNames[layerIndex - 1] for layerIndex in self.model.getUnconnectedOutLayers()]
        # yolo supports blob format of data as input so we are converting the image to blob type
        blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        # setting the blob as input
        self.model.setInput(blob)
        # forward pass means passing the input through all the layers of the model computing the output
        results = self.model.forward(outputLayers)
        # obtained results are rearranged for better accessability
        classIDs, confidences, boxes = self.getResults(results, image)
        classIDs = [*set(classIDs)]
        names = [self.classes[index] for index in classIDs]
        print(names)
        return names
