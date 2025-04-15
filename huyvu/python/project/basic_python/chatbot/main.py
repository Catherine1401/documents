import speech_recognition
import pyttsx3

voice = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print('iam listenning...')
    audio = voice.listen(mic)
try:
    input_text = voice.recognize_google(audio)
except:
    input_text = 'i do not understand, you can say that'
engine = pyttsx3.init()
engine.say(input_text)
engine.runAndWait()

    
