
from source_files.speech_recognizer import speech_recognizer
from source_files.text_preprocessor import text_preprocessor
from source_files.serial_communication import SerialCommunication
if __name__ == '__main__':
    speech_recognizer_instance = speech_recognizer()
    text_preprocessor_instance = text_preprocessor()

    while True:
        
        serial_port = SerialCommunication()
        text = speech_recognizer_instance.recognize_speech_input()
        playBack, command, sendToArduino = text_preprocessor_instance.process_text(text)
        if playBack:
            if sendToArduino:
                if command is not None:
                    command = command+"\n"
                    serial_port.write(command.encode('utf-8'))
            speech_recognizer_instance.playback(command)
            print(command)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
