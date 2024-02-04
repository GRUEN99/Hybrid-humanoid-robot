from gtts import gTTS
import speech_recognition as sr
import pygame
import time
import os
from io import BytesIO
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

class speech_recognizer:
    pygame.init()
    pygame.mixer.init(frequency=32000)
    def __init__(self):
        GPIO.setmode (GPIO.BOARD)
        self.VOICE_INPUT_PIN = 8
        GPIO.setup (self.VOICE_INPUT_PIN,GPIO.OUT)
        pass

    def recognize_speech_input(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            GPIO.output(self.VOICE_INPUT_PIN,GPIO.HIGH)
            audio = r.listen(source , phrase_time_limit=5)

            try:
                print("Recognizing...")
                GPIO.output(self.VOICE_INPUT_PIN,GPIO.LOW)
                input_from_user = r.recognize_google(audio, language='en-US')
                print(f"User said: {input_from_user}\n")
            except Exception as e:
                print(e)
                print("Unable to Recognize your voice.")
                return "None"

            return input_from_user


    def playback(self , text):
        #a = time.time()
        if 'text.mp3' in os.listdir():
            os.remove("text.mp3")
        language = 'en-US'
        try:
            speech = gTTS(text=text, lang=language, slow=False)
            mp3_fo = BytesIO()
            speech.write_to_fp(mp3_fo)
            mp3_fo.seek(0)
            pygame.mixer.init()
            pygame.mixer.music.load(mp3_fo)
            
            pygame.mixer.music.play()
            #print(time.time() - a)
            while pygame.mixer.music.get_busy() == True:
                continue
        except Exception as e:
            print(e)
            pass



