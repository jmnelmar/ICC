from gtts import gTTS
from io import BytesIO
from pygame import mixer
import speech_recognition
import sounddevice
import pyttsx3


import time

def speak(str):
    mp3_fp = BytesIO()
    tts = gTTS(str, lang='en')
    tts.write_to_fp(mp3_fp)
    return mp3_fp

def speech_to_text():
    recognizer = speech_recognition.Recognizer()
    
    with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)    
    try:
        text = recognizer.recognize_google(audio)
        #text = text.lower()
        print(f"Recognized {text}")
        text_to_speech(text)
    except:
        recognizer = speech_recognition.Recognizer()

    '''recognizer = speech_recognition.Recognizer()
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic) 
                text = recognizer.recognize_google(audio)
                text = text.lower()
                print(f"Recognized {text}")
        except:
            recognizer = speech_recognition.Recognizer()
            continue'''

def text_to_speech(str):
    mixer.init()
    while(1):
    #str = input("introduce text to speech - type exit to terminate the program\n")
    #if str == "exit":
    #        break
        sound = speak(str)
        sound.seek(0)
        mixer.music.load(sound, "mp3")
        mixer.music.play()
        time.sleep(1)

speech_to_text()