import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import rawsteelp


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("  good morning sunshine!")

    elif hour >= 12 and hour < 18:
        speak(" ... good afternoon !")

    else:
        speak("  good evening!")

    speak(" ... welcome to digital A I created by mr.prem!!!  I am rio. at your service...how may i help you!  ")


def takeCommand():
    # takes command from user using mircophone

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 500
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}\n ')

    except Exception as e:
        print(e)
        print("say that again...")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia ")
            print(results)
            speak(results)
            quit()

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            quit()

        elif 'open google' in query:
            webbrowser.open('google.com')
            quit()
        