import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition

import speech_recognition as sr

import pywhatkit as kit

engine = pyttsx3.init()

voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)



r = sr.Recognizer()

with sr.Microphone() as source:
    engine.say("Say the word")
    engine.runAndWait()
    print('Listening.....')

    audio = r.listen(source)

try:
    print('Recognising...')
    query = r.recognize_google(audio, language='en')

    if 'play' in query:
        query = query.replace('play', "")
        kit.playonyt(query)
        query = 'Playing' + query
    elif 'weather' in query:
        query = 'Opening current weather in browser'
        kit.search('current weather')

    engine.say(query)
    engine.runAndWait()
 

except Exception as e:
    print('exception : ',e)