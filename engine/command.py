import pyttsx3
import speech_recognition as sr
import eel

eel.init('www')

@eel.expose
def speak(text):

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=6)
            text = r.recognize_google(audio)
            print(f"User said: {text}")
            speak(text)  
            return text
        except sr.WaitTimeoutError:
            return speak("Listening timed out. Please speak again")
        except sr.UnknownValueError:
            return speak("Sorry, I could not understand the audio")
        except sr.RequestError as e:
            return speak(f"Could not request results from Google Speech Recognition service; {e}")


