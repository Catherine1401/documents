import speech_recognition

voice = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print('iam listenning...')
    audio = voice.listen(mic)
input_text = voice.recognize_google(audio)
print(input_text)

