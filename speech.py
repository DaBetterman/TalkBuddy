import speech_recognition as sr
import pyttsx3
# import pyaudio

engine = pyttsx3.init() #'sapi5'
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def hearing():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
        try:
            print("Wait for a few moments...")
            query = r.recognize_google(audio, language='en-us')
            print(f"You just said: {query}\n")
            if query.strip():
                return query.lower()
            else:
                print("Did not catch that. Please speak again.")
                speak("Did not catch that. Please speak again.")
        except sr.UnknownValueError:
            print("Could not understand audio. Please try again.")
            speak("Could not understand audio. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak(f"Could not request results from Google Speech Recognition service; {e}")
            break