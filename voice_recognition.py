import speech_recognition as sr
import pyttsx3
import subprocess

# Initialize Speech Recognizer & Speaker
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set TTS Voice (Optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change index if needed

def speak(text):
    """Text-to-Speech Function"""
    engine.say(text)
    engine.runAndWait()

def listen_for_command():
    """Listen for Voice Command"""
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).upper()
        print(f"🔊 You said: {command}")
        return command
    except sr.UnknownValueError:
        print("❌ Could not understand")
        return ""
    except sr.RequestError:
        print("❌ API Error")
        return ""

if __name__ == "__main__":
    while True:
        command = listen_for_command()

        if "ACCOUNTANT MJ" in command:
            speak("Hello, I am Accountant MJ! How can I assist you?")
        
        elif "PLAY MUSIC" in command:
            speak("Playing Music...")
            print("🎵 Playing Music...")
            subprocess.run(["mpv", "test.mp3"])
        
        elif "STOP" in command:
            speak("Stopping everything!")
            print("🛑 Stopping...")
            break
        
        elif "HELLO" in command:
            speak("Hello! How are you?")
        
        elif command:
            speak(f"You said: {command}")
