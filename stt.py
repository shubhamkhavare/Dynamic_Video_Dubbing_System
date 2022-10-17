import speech_recognition as sr
import translators as ts
from gtts import gTTS
import os
r = sr.Recognizer()

# TRANSLATION
file_audio = sr.AudioFile('Output/abcd.wav')

with file_audio as source:
   audio_text = r.record(source)


eng = r.recognize_google(audio_text)
print(eng)

trans = ts.google(eng, from_language='en', to_language='hi')
print(trans)

# TTS

myobj = gTTS(text=trans, lang='hi', slow=False)

myobj.save("Output/translated.mp3")
