# Library Function Declare
import datetime
import pyttsx3 
import speech_recognition as sr

# Voice Cover
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Speak Content
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak('I am Bishal Naskar. How can I help you?')

# Speech Recognition
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source, timeout=33333333, phrase_time_limit=20)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        return None
    query =query.lower()
    return query

# Speak Output by Fuunction Declaring [Main Function]
if __name__=="__main__":
    speak('Hello')
    wishMe()
    takeCommand()
