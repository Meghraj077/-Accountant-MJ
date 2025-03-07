import os
import time
import json
import subprocess
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Load API keys from config and env files (securely)
def load_api_keys():
    paths = ["config", "env"]
    api_keys = {}
    for path in paths:
        if os.path.exists(path):
            with open(path, "r") as f:
                lines = f.readlines()
                for line in lines:
                    key, value = line.strip().split("=")
                    api_keys[key] = value
    return api_keys

API_KEYS = load_api_keys()

# Ensure pulseaudio is running
def start_pulseaudio():
    subprocess.run(["pulseaudio", "--start"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Convert text to speech
def speak(text):
    try:
        tts = gTTS(text=text, lang="en")
        tts.save("response.mp3")
        play(AudioSegment.from_file("response.mp3", format="mp3"))
    except Exception as e:
        print(f"Error in speech synthesis: {e}")

# Record and recognize voice
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand."
    except sr.RequestError:
        return "API request failed."

# Background process to keep listening
def voice_assistant_loop():
    start_pulseaudio()
    while True:
        command = recognize_speech()
        print(f"You said: {command}")

        if "exit" in command.lower():
            speak("Goodbye!")
            break
        elif "hello" in command.lower():
            speak("Hello! How can I help you?")
        else:
            speak("I didn't catch that.")

if __name__ == "__main__":
    voice_assistant_loop()
