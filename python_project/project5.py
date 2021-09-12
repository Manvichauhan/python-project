from math import trunc
from pyttsx3 import engine, speak
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import pywhatkit
import datetime

r=sr.Recognizer()

def speakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def Takecom(): #work for hearing
    try:
        with sr.Microphone() as b:
            # wait for the recognizer to adjust the energy threshold
            r.adjust_for_ambient_noise(b,duration=0.3)
            #listen to the input from user
            print("I am listening")
            audio2=r.listen(b)
            # using google to recognize audio

            mytext = r.recognize_google(audio2)

            mytext = mytext.lower()
            print(mytext)
            #speakText(mytext)

    except sr.RequestError as e:
        print("Could Not request Result; {0}".format(engine))
    except Exception: #For error handling
        speak("error...")
        print("Network connection error") 
        return "none"
    return  mytext

#speakText('Hello Manvi')

def Task():

    def wish():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon!")
        else:
            speak("Good Evening!")

    def music():
        speak('tell me the name of the song')
        musicname=Takecom()

        if 'man' in musicname:
            os.startfile('[Songs.PK] Aashiqui 2 - 01 - Tum Hi Ho.mp3')
        else:
            pywhatkit.playonyt(musicname)
        speak('your song has been started,enjoy maam')

    def openApps():
       # q=Takecom()
        speak('okk sir! wait a minute')  
        if 'open pycharm'  in  query:
            os.startfile('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe')

        # elif 'open vlc' in query:
        #     os.startfile('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe')
        speak('your command hasbeen completed sir')

    def closeApp():
        speak('okk sir wait a second')
        if 'close app'  in  query:
            os.startfile('C:\\Users\\manvi chauhan\\AppData\\Local\\Programs\\Microsoft VS Code')
        elif 'close chrome' in query:
            os.startfile('chrome')
        elif 'close youtube' in query:
            os.system('https://www.youtube.com/')
             
             


            
    wish()  


    while True:
        query=Takecom()

        if 'Hello Jarvis' in query:
            speak("hello Manvi, I am Jarvis.")
            speak("your Personal Assistant")
            speak("how may i help you.")
        elif "how are you" in query:
            speak("I am fine")
            speak("what about you.")

        elif "Good night" in query:
            speak("Good night Manvi Ma'am")

        elif "about python" in query:
            speak("pythonn was created by guido van rossum, and first")
            
        elif "open youtube" in query:
            speak("okk sir")
            webbrowser.open('https://www.youtube.com/')
            speak('done sir')
        elif "open Facebook" in query:
            speak("okk sir")
            webbrowser.open('https://www.facebook.com/')
            speak('done sir')
        elif "open mail" in query:
            speak("okk sir")
            webbrowser.open('https://mail.google.com/mail/u/1/#inbox')
            speak('done sir')

        elif "play music" in query:
            music()

        elif "open vlc"   in query:
            openApps()
        # elif "open vlc"   in query:
        #     openApps()
        elif "close app"   in query:
            closeApp()

        elif "close chrome"   in query:
            closeApp()

        elif "close youtube"   in query:
            closeApp()
Task()

