from __future__ import print_function
import speech_recognition as sr
import os
import time
from gtts import gTTS
import datetime
import warnings
import pyjokes
import webbrowser
import calendar
import pyttsx3
import random
import smtplib
import wikipedia
import playsound
import wolframalpha
import requests
import json
import winshell
import subprocess
import ctypes
from twilio.rest import Client
import pickle
import os.path
import openai
from pygame import mixer
from pynput.keyboard import Key,Controller
from time import sleep



warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def talk(audio):
    engine.say(audio)
    engine.runAndWait()



def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recog.listen(source)

    data = " "

    try:
        data = recog.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Assistant could not understand the audio")
    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition" + ex)

    return data





def response(text):
    print(text)
    tts = gTTS(text=text, lang="en")
    audio = "Audio.mp3"
    tts.save(audio)
    playsound.playsound(audio)
    os.remove(audio)


def call(text):
    action_call = "hey sara"

    text = text.lower()

    if action_call in text:
        return True

    return False


def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return "Today is " + week_now + ", " + months[month_now - 1]  + ordinals[day_now - 1] + "."


def say_hello(text):
    greet = ["hi", "hola", "greetings", "wassup", "hello"]

    response = ["howdy,How can I help you", "whats good,How can I help you", "hello,How can I help you", "hey there,How can I help you"]

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + "."

    return ""


def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "who" and list_wiki[i + 1].lower() == "is":
            return list_wiki[i + 2] + " " + list_wiki[i + 3]



def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


keyboard = Controller()
def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)





    # Enable low security in gmail
    #server.login("koushikdandi@gmail.com", "koushik@143")
   # server.sendmail("koushik@gmail.com", to, content)
   # server.close()

while True:

    try:
        text = rec_audio()
        speak = " "

        if call(text):

            speak = speak + say_hello(text)

            if "date" in text or "day" in text or "month" in text:
                get_today = today_date()
                speak = speak + " " + get_today

            elif "time" in text:
                now = datetime.datetime.now()
                meridiem = ""
                if now.hour >= 12:
                    meridiem = "pm"
                    hour = now.hour - 12
                else:
                    meridiem = "am"
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + "It is " + str(hour) + ":" + minute + " " + meridiem + " ."

            elif "wikipedia" in text or "Wikipedia" in text:
                if "who is" in text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary(person, sentences=2)
                    speak = speak + " " + wiki


            
            elif "who are you" in text or "define yourself" in text:
                speak = speak + "Hello, I am Sara. Your Assistant. I am here to make your life easier. You can command me to perform various tasks such as asking questions or opening applications etcetera"

            elif "made you" in text or "created you" in text:
                speak = speak + "I was created by Kaushik"

            elif "your name" in text:
                speak = speak + "My name is Sara"

            elif "who am I" in text:
                speak = speak + "You must probably be a human"

            elif "why do you exist" in text or "why did you come to this word" in text:
                speak = speak + "It is a secret"

            elif "how are you" in text:
                speak = speak + "I am awesome, Thank you"
                speak = speak + "\nHow are you?"

            elif "fine" in text or "good" in text:
                speak = speak + "It's good to know that your fine"

            elif "tired" in text:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=E3jOYQGu1uw&t=1246s&ab_channel=scientificoder")
                    
            elif "open" in text.lower():
                if "chrome" in text.lower():
                    speak = speak + "Opening Google Chrome"
                    os.startfile(
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                    )

                elif "word" in text.lower():
                    speak = speak + "Opening Microsoft Word"
                    os.startfile (
                        r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
                    )

                elif "excel" in text.lower():
                    speak = speak + "Opening Microsoft Excel"
                    os.startfile(
                        r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
                    )

                elif "vs code" in text.lower():
                    speak = speak + "Opening Visual Studio Code"
                    os.startfile(
                        r"C:\Users\sunee\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                    )

                elif "youtube" in text.lower():
                    speak = speak + "Opening Youtube\n"
                    webbrowser.open("https://youtube.com/")

                elif "google" in text.lower():
                    speak = speak + "Opening Google\n"
                    webbrowser.open("https://google.com/")

                elif "stackoverflow" in text.lower():
                    speak = speak + "Opening StackOverFlow"
                    webbrowser.open("https://stackoverflow.com/")

                elif "channel" in text.lower():
                    ind = text.lower().split().index("channel")
                    search = text.split()[ind + 1:]
                    webbrowser.open(
                        "http://www.youtube.com/results?search_query=" +
                        "+".join(search)
                    )
                    speak = speak + "Opening " + str(search) 

                else:
                    speak = speak + "Application not available"

            
            elif "search" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search))
                speak = speak + "Searching " + str(search) + " on google"

            elif "google" in text.lower():
                ind = text.lower().split().index("google")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search))
                speak = speak + "Searching " + str(search) + " on google"

            elif "change background" in text or "change wallpaper" in text:
                img = r"C:\Users\sunee\OneDrive - iTouch Solutions\Pictures\wallpapers"
                list_img = os.listdir(img)
                imgChoice = random.choice(list_img)
                randomImg = os.path.join(img, imgChoice)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                speak = speak + "Background changed successfully"

            elif "play music" in text or "play song" in text:
                talk("Here you go with music")
                music_dir = r'C:\Users\sunee\Music\music'
                songs = os.listdir(music_dir)
                d = random.choice(songs)
                random = os.path.join(music_dir, d)
                playsound.playsound(random)

            elif "empty recycle bin" in text:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                speak = speak + "Recycle Bin Emptied"

            elif "where is" in text:
                ind = text.lower().split().index("is")
                location = text.split()[ind + 1:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                speak = speak + "This is where " + str(location) + " is."
                webbrowser.open(url)

            elif "joke" in text:
                speak = speak + pyjokes.get_joke()

            elif "make a note" in text:
                talk("What would you like me to write down?")
                note_text = rec_audio()
                note(note_text)
                speak = speak + "I have made a note of that."

            
            elif "what is the weather in" in text:
                key = "ae7bcb791c6fc835b12c6368048b53f7"
                weather_url = "http://api.openweathermap.org/data/2.5/weather?"
                ind = text.split().index("in")
                location = text.split()[ind + 1:]
                location = "".join(location)
                url = weather_url + "appid=" + key + "&q=" + location
                js = requests.get(url).json()
                if js["cod"] != "404":
                    weather = js["main"]
                    temperature = weather["temp"]
                    temperature = temperature - 273.15
                    humidity = weather["humidity"]
                    desc = js["weather"][0]["description"]
                    weatherResponse = " The temperature in Celcius is " + str(temperature) + " The humidity is " + str(
                        humidity) + " and The weather description is " + str(desc)
                    speak = speak + weatherResponse
                else:
                    speak = speak + "City Not Found"


     
            elif "what is" in text or "who is" in text:
                ind = text.lower().split().index("is")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search))
                speak = speak + "Searching " + str(search) + " on google"

            elif "play a game" in text:
                 from game import game_play
                 game_play()
                 break
            elif "shutdown system" in text:
                    ind = text.lower().split().index("system")

                    talk("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break
            elif "calculate" in text:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    text = text.replace("calculate","")
                    text = text.replace("sara","")
                    Calc(text)
                    break

 







            response(speak)
    except:
        talk("I don't understand that")