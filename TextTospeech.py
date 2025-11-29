import matplotlib.pyplot as plt 
import pyttsx3 
import speech_recognition as sr
import webbrowser
import os 
import pywhatkit 

speaker = pyttsx3.init()
mic = sr.Recognizer()

speaker.say("Welcome to Jarvis..")
speaker.runAndWait()

with sr.Microphone() as source:
    print("Start speaking...")
    voice = mic.listen(source)
    text = mic.recognize_google(voice)
    

if "open Notepad" in text:
    print("Opening Notepad...")
    os.system("Notepad")

# elif "send message"in text:
#     print("sending message..")

elif "open edge" in text:
  print("Opening Edge...")
  os.system("start msedge")

# pywhatkit.sendwhatmsg_instantly("+918102092566","hii debo") 
elif "open netflix" in text:
    print("Opening Netflix...")
    os.system('start msedge "https://www.netflix.com"')