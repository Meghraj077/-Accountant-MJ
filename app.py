import os
import requests
import pyttsx3
import speech_recognition as sr
import traceback
import json
from flask import Flask, jsonify, request
from dotenv import load_dotenv

# 🔹 Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# 🔹 Initialize Flask App
app = Flask(__name__)

# ✅ AI Voice Assistant - Text-to-Speech (TTS)
engine = pyttsx3.init(driverName='espeak')

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello, Accountant MJ is ready!")

# ✅ AI Voice Command System
recognizer = sr.Recognizer()

def listen_command():
    with sr.Microphone() as source:
        speak("Listening for your command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        speak(f"You said: {command}")
        return command
    except:
        return ""

# ✅ Dynamic Feature Management
features = {
    "gst": "calculate_gst",
    "stock": "get_stock_price",
    "call": "phone_control",
    "sms": "phone_control",
    "alarm": "phone_control",
    "translate": "translate_text"
}

def add_feature(name, function_code):
    try:
        exec(function_code, globals())  # Add function dynamically
        features[name] = name
        speak(f"Feature {name} added successfully!")
        return {"status": "Success", "message": f"Feature '{name}' added."}
    except Exception as e:
        return {"error": str(e)}

# ✅ AI-Based Accounting Automation (GST Calculation)
def calculate_gst(amount):
    gst_rate = 18
    gst_amount = (amount * gst_rate) / 100
    return {"amount": amount, "GST": gst_amount, "Total": amount + gst_amount}

# ✅ AI-Based Stock Market Analysis
def get_stock_price(symbol):
    stock_data = {
        "AAPL": 175.23,
        "GOOGL": 2834.50,
        "TSLA": 812.30
    }
    return {"Stock": symbol, "Price": stock_data.get(symbol.upper(), "Not Found")}

# ✅ AI Voice Assistant - Phone Control
def phone_control(command):
    actions = {
        "call": "Calling...",
        "sms": "Sending SMS...",
        "alarm": "Setting Alarm..."
    }
    return {"Command": command, "Action": actions.get(command.lower(), "Invalid Command")}

# ✅ AI-Powered Translator (Real-Time)
def translate_text(text, target_lang="hi"):
    return {"text": text, "translated": f"({target_lang}) {text} (Translated)"}

# ✅ Flask Routes
@app.route('/')
def home():
    return jsonify({"message": "🚀 Accountant-MJ API is Running!"})

@app.route('/add_feature', methods=['POST'])
def add_new_feature():
    try:
        data = request.get_json()
        name = data.get("name")
        function_code = data.get("code")

        if name and function_code:
            return jsonify(add_feature(name, function_code))
        else:
            return jsonify({"error": "Invalid request format."})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/execute/<feature>', methods=['POST'])
def execute_feature(feature):
    try:
        if feature in features:
            func = globals().get(features[feature])
            if func:
                return jsonify(func())
            else:
                return jsonify({"error": "Feature exists but function not found."})
        else:
            return jsonify({"error": "Feature not found."})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/voice_add', methods=['GET'])
def voice_add_feature():
    speak("What feature do you want to add?")
    command = listen_command()

    if command:
        new_code = f"def {command.replace(' ', '_')}(): return {{'message': 'New feature {command} added!'}}"
        return jsonify(add_feature(command.replace(" ", "_"), new_code))
    else:
        return jsonify({"error": "Could not recognize command."})

# ✅ Start Flask Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
