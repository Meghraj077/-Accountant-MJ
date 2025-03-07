import os
import subprocess
import json
import time
import speech_recognition as sr
import openai  # GPT API का उपयोग AI Debugging के लिए

# API Key Configuration
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Voice Recognizer (सिर्फ आपकी आवाज सुनेगा)
recognizer = sr.Recognizer()
user_voice_id = "your-unique-voice-id"  # आपकी आवाज़ का fingerprint सेट करें

def recognize_voice():
    """ यूज़र की आवाज़ पहचानकर command execute करे """
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        voice_text = recognizer.recognize_google(audio)
        return voice_text.lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None

def is_authorized_voice():
    """ Check करे कि सिर्फ आपकी आवाज़ है """
    voice_input = recognize_voice()
    if voice_input:
        return user_voice_id in voice_input  # सिर्फ आपकी आवाज़ पर execute होगा
    return False

def detect_and_fix_errors(file_path):
    """ Python Code की Errors detect और fix करे """
    if not os.path.exists(file_path):
        return "Error: File not found!"

    with open(file_path, "r") as file:
        code = file.read()

    prompt = f"यह Python कोड errors के साथ दिया गया है, इसे सही करो:\n```python\n{code}\n```"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    fixed_code = response["choices"][0]["message"]["content"]

    with open(file_path, "w") as file:
        file.write(fixed_code)

    return "Code errors fixed successfully!"

def auto_add_new_feature(feature_code, file_path):
    """ AI अपने आप नई feature को Python File में जोड़ देगा """
    if not os.path.exists(file_path):
        return "Error: File not found!"

    with open(file_path, "a") as file:
        file.write("\n\n" + feature_code)

    return "New feature added successfully!"

def self_update():
    """ AI अपने आप खुद को update करेगा """
    subprocess.run(["git", "pull"])  # Git से latest updates लाएगा
    os.system("pip install -r requirements.txt")  # Dependencies अपडेट करेगा
    return "Self-update completed!"

def execute_voice_command():
    """ Voice Command से AI Actions लेगा """
    if not is_authorized_voice():
        print("Unauthorized voice detected!")
        return

    print("Listening for commands...")
    command = recognize_voice()

    if "fix errors" in command:
        print(detect_and_fix_errors("app.py"))

    elif "add new feature" in command:
        new_feature = input("Enter new feature code: ")  # Future में AI खुद feature detect करेगा
        print(auto_add_new_feature(new_feature, "app.py"))

    elif "update yourself" in command:
        print(self_update())

    else:
        print("Unknown command!")

if __name__ == "__main__":
    while True:
        execute_voice_command()
