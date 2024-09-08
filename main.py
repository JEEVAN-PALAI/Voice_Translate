import speech_recognition as SR
from googletrans import Translator
import pyttsx3

recognizer = SR.Recognizer()
engine = pyttsx3.init()

with SR.Microphone() as source:
    print("Clear the background noises..")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Waiting For Your Voice..")
    audio = recognizer.listen(source)
    print("Recording Done..")

try:
    print("Recognizing..")
    result = recognizer.recognize_google(audio, language='en')
    print(f"You said: {result}")
except Exception as e:
    print(f"Error recognizing audio: {e}")

def transpo():
    langinput = input("In which language do you want to translate the voice (e.g.,'fr' for French, 'es' for Spanish): ").strip()
    if not langinput:
        print("No language provided. Please try again.")
        return
    translator = Translator()
    try:
        translate_text = translator.translate(result, dest=langinput).text
        print(f"Translated text: {translate_text}")
        engine.say(translate_text)
        engine.runAndWait()
    except Exception as e:
        print(f"Translation error: {e}")

transpo()
