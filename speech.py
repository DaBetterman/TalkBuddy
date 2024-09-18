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

# import speech_recognition as sr
# from gtts import gTTS
# import pygame
# import os

# def speak(text):
#     # Create a gTTS object
#     tts = gTTS(text, lang='en')

#     # Save the audio to a temporary file
#     temp_file = "/tmp/temp_audio.mp3"
#     tts.save(temp_file)

#     # Initialize pygame mixer
#     pygame.mixer.init()

#     # Load the temporary file
#     pygame.mixer.music.load(temp_file)

#     # Play the audio
#     pygame.mixer.music.play()

#     # Wait until the audio is finished playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)

#     # Remove the temporary file
#     os.remove(temp_file)

# def hearing():
#     r = sr.Recognizer()
#     while True:
#         with sr.Microphone() as source:
#             print("Listening...")
#             r.pause_threshold = 1
#             r.adjust_for_ambient_noise(source, duration=1)
#             audio = r.listen(source)
#         try:
#             print("Wait for a few moments...")
#             query = r.recognize_google(audio, language='en-us')
#             print(f"You just said: {query}\n")
#             if query.strip():
#                 return query.lower()
#             else:
#                 print("Did not catch that. Please speak again.")
#                 speak("Did not catch that. Please speak again.")
#         except sr.UnknownValueError:
#             print("Could not understand audio. Please try again.")
#             speak("Could not understand audio. Please try again.")
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Speech Recognition service; {e}")
#             speak(f"Could not request results from Google Speech Recognition service; {e}")
#             break

# # Example usage
# if __name__ == "__main__":
#     speak("Hello, this is a test of the gTTS library with pygame.")
