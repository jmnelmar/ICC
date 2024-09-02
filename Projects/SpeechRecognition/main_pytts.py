import speech_recognition
import pyttsx3
import sounddevice

engine = pyttsx3.init()

def speech_to_text():
    recognizer = speech_recognition.Recognizer()

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
            continue

def text_to_speech(str):
    while(1):
        str = input("Enter something - type exit to close the program\n")
        engine.setProperty('rate',180)
        if str == "exit":
            break
        engine.say(str)
        engine.runAndWait()

def voices():
    voices = engine.getProperty('voices')
    
    for voice in voices:
        if voice.getProperty('language') == u'en_US':
            print(voice, voice.id)
            engine.setProperty('voice', voice.id)
            engine.setProperty('rate',150)
            engine.setProperty('rate',150)
            engine.setProperty('gender','female')
            engine.say("Hello World!")
            engine.runAndWait()
            engine.stop()

def speech():
    rec = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        print('Say something')
        audio = rec.listen(source)
        print("Done")
    try:
        text = rec.recognize_google(audio)
        print(f'google think you said\n {text}')
        
    except Exception as e:
        print(e)

str = "You are so cool"
speech()
#text_to_speech(str)
#voices()