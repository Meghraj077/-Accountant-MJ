import speech_recognition as sr
from gtts import gTTS
import os

def text_to_speech(text, lang="en"):
    """ टेक्स्ट को Voice में Convert करें """
    speech = gTTS(text=text, lang=lang, slow=False)
    speech.save("output.mp3")
    os.system("termux-media-player play output.mp3")

def voice_translation():
    """ Voice Recognition & Translation """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for translation...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        text_to_speech(text, lang="hi")  # Hindi में Convert

    except:
        print("Sorry, समझ नहीं पाया!")

if __name__ == "__main__":
    voice_translation()
