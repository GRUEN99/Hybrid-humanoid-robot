import datetime
from source_files.weather import get_Weather_report
#from source_files.face_recognizer import FaceRecognizer
#from source_files.object_detector import ObjectDetector
import time

class text_preprocessor:
    def __init__(self):
        pass
        #self.face_recognizer = FaceRecognizer()
        #self.object_detector = ObjectDetector()
        

    def process_text(self , text):
        try:
            text = text.lower()
            playBack = False
            command = "not found"
            sendToArduino = False
            if "robot" in text:
                try:
                    _ , command = text.split("robot")
                    command = self.setCommand(command)
                    playBack = True
                    sendToArduino = True
                except:
                    playBack = False
                    command = "not found"
                    sendToArduino = False


            if ("hi" in text or "hello" in text or "hai" in text) and "this" not in text:
                playBack = True
                command = "hello , How can I help You?"
                sendToArduino = False
            elif "how are you" in text:
                playBack = True
                sendToArduino = False
                command = "I am good , How can I help You?"
            elif "time" in text:
                playBack = True
                sendToArduino = False
                current_date_time = datetime.datetime.now()
                command = "Current time is " + current_date_time.strftime("%H:%M:%S")

            elif "date" in text:
                playBack = True
                sendToArduino = False
                current_date = datetime.date.today()
                command = "Current date is " + current_date.strftime("%B %d, %Y")

            elif "weather" in text:
                playBack = True
                sendToArduino = False
                temperature , sky = get_Weather_report()
                command = "temperature is {temp} , sky is {sky}".format(temp = temperature , sky = sky)

#             elif "who" in text and "i" in text and "am" in text:
#                 playBack = True
#                 sendToArduino = False
#                 now = time.time()
#                 while time.time() - now <= 5:
#                     flag , image = self.face_recognizer.VISUALS.read()
#                     if flag:
#                         names = self.face_recognizer.recognizeFaces(image)
#                         print(names)
#                         if 'Unknown' not in names:
#                             command = "Hai {name} , How Can I Help you?".format(name = names[0])
#                             break
                        
#             elif "what is this" in text:
#                 playBack = True
#                 sendToArduino = False
#                 now = time.time()
#                 while time.time() - now <= 5:
#                     flag , image = self.face_recognizer.VISUALS.read()
#                     if flag:
#                         names = self.object_detector.detectObjects(image)
#                         if len(names) == 0 :
#                             command = "no object Detected"
#                             continue
#                         command = "{number} objects detected ".format(number = len(names))
#                         for index , name in enumerate(names):
#                             command = command + str(index+1) +" is " +name
#                         break
            
            return playBack , command , sendToArduino

        except Exception as e:
            print(e)
            return False , "not found" , False


    def setCommand(self , command):
        if "move forward" in command:
            return "move forward"
        elif "slide left" in command or "left" in command:
            return "slide left"
        elif "slide right" in command or "right" in command:
            return "slide right"
        elif "da" in command:
            return "dab"
        elif "stop" in command:
            return "stop"










