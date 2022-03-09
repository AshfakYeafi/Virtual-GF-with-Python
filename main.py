import speech_recognition as sr
import pyttsx3
import random
import datetime
import time as t
import webbrowser
import wikipedia
import csv
import os
import cv2
import pyaudio
import playsound
from PIL import ImageTk,Image
import tkinter as ttk
import json
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

from google_speech import Speech

# logging.basicConfig(level=logging.INFO)


# chatbot = ChatBot('e bot')
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train(
#     'chatterbot.corpus.english'
#
# )
# lang = "en"
# audio="Fuck you"
# sp=Speech(audio, lang)
# sp.play()

start=True

gf_msg={"hello":"hi Baby",
        "i love you":"i love you too"
        }

def get_command():
    r=sr.Recognizer()
    r.pause_threshold=0.8
    r.energy_threshold=300
    with sr.Microphone() as source:
        audio=r.listen(source)
    try:
        quary=r.recognize_google(audio,language="en-in")
    except:
        return "None"
    return str(quary.lower())
def com_say(txt):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'english_rp+f3')
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    engine.say(txt)
    engine.runAndWait()

while start:
    txt=get_command()
    print(txt)
    if txt in gf_msg.keys():
        com_say(gf_msg.get(txt))
    start=False


