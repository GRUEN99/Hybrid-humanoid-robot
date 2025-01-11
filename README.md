# ServoAI fusion Robot
OVERVIEW
This project showcases the development of a hybrid humanoid robot capable of interacting with its environment and users through advanced technologies. The robot integrates facial recognition, object detection, voice command-based movement, and speech recognition functionalities, providing a comprehensive and interactive experience.


FEATURES
1. Face Recognition:
The robot incorporates a face recognition opencv and numpy modules. It can identify and track faces in real-time, enabling personalized interactions with individuals.
2. Object Detection:
Utilizing computer vision techniques and yolo algorithm the robot can detect and recognize objects in its surroundings. Further we have used coco dataset to train the model.
3. Voice Command-Based Movement:
The robot responds to voice commands for navigation and movement. And using speech recognition, pygame the robot can also say the current weather status ,date and time. Mainly the commandas as "Robot slide left ", "Robot slide right", "Robot move forward", upon questioning like what is the time ,date, weather the macgine provides the answer. To make things more interesting our robot can also dab upon the command "Robot dab".
4. Speech Recognition:
Integrated with a robust speech recognition system, the robot can also say the current weather status ,date and time upon using the specific modules.


TECHNOLOGY STACK 
Programming Language: mainly python 
Hardware Components: Raspberry pi 4 , servo controller, raspberry pi camera, 15 dual shaft metal gear servos and a bluetooth speeker clubz mini for voice (output), mAH 2000 battery .


SETUP INSTRUCTIONS
HARDWARE SETUP: The skeleton was ordered online . All the servo motors were placed and and the movements were done using a tool called robokits arduino usb servo controller. All the servos are attached to the servo controller which is inturn connected to the raspberry pi and the communication takes place through serial communication.
SOFTWARE SETUP: The coding language used is python and all the files are uploaded in raspberry pi . The main.py is runned to recieve the output.


FUTURE ENHANCEMENTS 
This project serves as a foundation for future enhancements and improvements. Potential enhancements may include:
Integration of additional sensors for environmental awareness.
Implementation of more advanced machine learning models for enhanced recognition tasks.
Expansion of the robot's capabilities through additional features and modules.


NOTE
1. The images for facial recognition should be saved in user_images folder with name that the robot needs to recognise with.
2. Run the main.py for output.
