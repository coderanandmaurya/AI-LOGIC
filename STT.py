# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 12:00:35 2021

@author: Anand Maurya
"""
import speech_recognition as sr
print(sr.__version__)
r = sr.Recognizer()

file_audio = sr.AudioFile('STT.wav')

with file_audio as source:
   audio_text = r.record(source)

print(type(audio_text))

print(r.recognize_google(audio_text))
