import speech_recognition as sr
import subprocess

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).upper()
        print(f"🔊 You said: {command}")
        return command
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

if __name__ == "__main__":
    command = listen_for_command()
    
    if "PLAY MUSIC" in command:
        print("🎵 Playing Music...")
        subprocess.run(["mpv", "test.mp3"])
    elif "STOP" in command:
        print("🛑 Stopping...")
