import os
import pyttsx3
import datetime
import webbrowser as wb
import speech_recognition as sr
tung = pyttsx3.init()
voice = tung.getProperty('voices')
tung.setProperty('voice', voice[0].id)

def speak(audio):
   print('tung: ' + audio)
   tung.say(audio)
   tung.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)
def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning Tung")
    elif hour >=12 and hour <= 18:
        speak("Good affternoon Tung")
    else:
        speak("Good night Tung")
    speak("How can i help you ?")

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language='en')
        print("Tony Lèo: " + query)
    except sr.UnknownValueError:
        print("Please")
        query = str(input("your order is: "))
    return query

if __name__ == "__main__":
    welcome()
    while True:

        query = command().lower()
        if "google" in query:
            speak("what should i search Tung ?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on google")
        if "youtube" in query:
            speak("what should i search Tung ?")
            search = command().lower()
            url = f"https://www.youtube.com//search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on youtube")
        elif "exit" in query:
            speak("Tung is exiting, good bye Tung")
            quit()