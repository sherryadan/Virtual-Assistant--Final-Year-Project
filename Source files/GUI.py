import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3
import sys
from httpx import get
import speech_recognition as sr
import opencloseapp
import playmusic
import openaiapi
import createfolder
import datetime
import searchbrowser
import datetimeweather
import webbrowser
import wikipedia
import threading
import latestnews

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hearing you......")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=4, phrase_time_limit=20)
        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}")
            return query
        except Exception as e:
            speak("Say that Again, Please")
            print(e)
            return "none"

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Adan")
    elif hour>=12 and hour<=18:
        speak("Good After Noon Adan")
    else:
        speak("Good Night Adan")
    speak("I am Sherry for your Service, How Can I help you Sir ")

def assistant_thread():
    wish()
    while True:
        query = takecommand().lower()
        if "open" in query:
            opencloseapp.open_application(query) #pass
        elif "close" in query:
            opencloseapp.close_application(query) #pass
        elif "Jarvis tell me" in query: 
            response=openaiapi.ask_question(query)
            speak(response)
            print(response)
        elif "play" in query:
            playmusic.play_song(query)  #pass
        elif "create new folder in C" in query: #PASS
            folder_name = query.replace("create new folder in C", "").strip()
            createfolder.create_folder_c(folder_name)
            speak("Folder created in C drive")
            print("Folder created in C drive")

        elif "create new folder in D" in query: #PASS
            folder_name = query.replace("create new folder in D", "").strip()
            createfolder.create_folder_d(folder_name)
            speak("Folder created in D drive")
            print("Folder created in D drive")

        elif "create new folder in desktop" in query: #PASS
            folder_name = query.replace("create new folder in desktop", "").strip()
            createfolder.create_folder_desktop(folder_name)
            speak("Folder created in Desktop")
            print("Folder created in Desktop")
        elif "search" in query:
            searchbrowser.search_query(query) #pass
        elif "date and time" in query:
            datetimeweather.get_current_datetime(query)
        elif "Weather" in query:
            datetimeweather.get_weather(query)
        elif "get ip address" in query: 
            ip = get('(https://api.ipify.org?format=text)').text
            speak(f"Your Ip address is {ip}")
        elif "wikipedia" in query: #pass
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wiki pedia {results}")
            print(results)
        elif "start instagram" in query:
            webbrowser.open("https://www.instagram.com/")
        elif "start facebook" in query:
            webbrowser.open("https://web.facebook.com/")
        elif "start twitter" in query:
            webbrowser.open("https://www.twitter.com/")
        elif "start youtube" in query:
            webbrowser.open("https://www.youtube.com/")
        elif "start skype" in query:
            webbrowser.open("https://www.skype.com/")
        elif "start gmail" in query:
            webbrowser.open("https://www.gmail.com/")
        elif "get latest news about technology" in query:
            latestnews.get_news('Technology')
        elif "get latest news about business" in query:
            latestnews.get_news('Business')
        elif "get latest news about sports" in query:
            latestnews.get_news('Sports')
        elif "get latest news about entertainment" in query:
            latestnews.get_news('Entertainment')
        elif "get latest news about politics" in query:
            latestnews.get_news('Politics')
        elif "get latest news about health" in query:
            latestnews.get_news('Health')
        elif "get latest news about science" in query:
            latestnews.get_news('Science')
        elif "no thanks" in query or "goodbye" in query:
                speak("Have A Good Day Sir")
                sys.exit()
        else:
            speak("Do you have any other work??")
            

class TerminalText(tk.Text):
    def write(self, text):
        self.insert(tk.END, text)
        self.see(tk.END)

window = tk.Tk()
window.title("Sherry")

terminal_output = TerminalText(window, height=10, width=40)
terminal_output.pack(side=tk.RIGHT, padx=10, pady=10)

sys.stdout = terminal_output

def start_assistant():
    thread = threading.Thread(target=assistant_thread)
    thread.start()

start_button = tk.Button(window, text="Start Assistant", command=start_assistant)
start_button.pack(side=tk.BOTTOM, padx=10, pady=10)

exit_button = tk.Button(window, text="Exit", command=window.destroy)
exit_button.pack(side=tk.BOTTOM, padx=10, pady=10)

window.mainloop()