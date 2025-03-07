from flask import Flask, request, jsonify
import os
import pyttsx3
import speech_recognition as sr
import json
import openai
from dotenv import load_dotenv

# ✅ Load API Key Securely (No Hardcoded API Key)
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

# ✅ AI Voice Assistant - Text-to-Speech (TTS)
try:
    engine = pyttsx3.init()
    engine.say("Hello, Accountant MJ is now active!")
    engine.runAndWait()
except:
    print("TTS Not Supported in Termux!")

# ✅ Self-Healing & Auto-Fix System
def self_healing(code):
    try:
        exec(code)
    except Exception as e:
        print(f"Error detected: {e}")
        fix_code = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Fix the given Python code."},
                {"role": "user", "content": f"Fix this code: {code}"}
            ]
        )
        new_code = fix_code['choices'][0]['message']['content']
        print("Fixed Code:\n", new_code)
        exec(new_code)

# ✅ AI-Based Accounting Automation (GST Calculation)
def calculate_gst(amount):
    gst_rate = 18
    gst_amount = (amount * gst_rate) / 100
    return {"amount": amount, "GST": gst_amount, "Total": amount + gst_amount}

# ✅ AI-Based Stock Market Analysis
def get_stock_price(symbol):
    stock_data = {"AAPL": 175.23, "GOOGL": 2834.50, "TSLA": 812.30}
    return {"Stock": symbol, "Price": stock_data.get(symbol.upper(), "Not Found")}

# ✅ AI Voice Assistant - Phone Control
def phone_control(command):
    actions = {"call": "Calling...", "sms": "Sending SMS...", "alarm": "Setting Alarm..."}
    return {"Command": command, "Action": actions.get(command, "Unknown Command")}

# ✅ AI-Powered Voice Command Processing
def listen_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"User Said: {command}")
        return {"status": "Success", "command": command}
    except Exception as e:
        return {"status": "Error", "message": str(e)}

# ✅ Self-Coding & Feature Addition
def add_new_feature(prompt):
    new_code = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Generate Python code for this feature."},
            {"role": "user", "content": f"Write code for: {prompt}"}
        ]
    )
    generated_code = new_code['choices'][0]['message']['content']
    print("New Feature Code:\n", generated_code)
    with open("features.py", "a") as file:
        file.write(f"\n# New Feature: {prompt}\n{generated_code}\n")

# ✅ Flask API Routes
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Accountant MJ API is Running!"})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Running", "message": "System is Healthy"})

@app.route("/update", methods=["POST"])
def update():
    data = request.get_json()
    return jsonify(self_healing(data["new_code"]))

@app.route("/gst", methods=["POST"])
def gst():
    data = request.get_json()
    return jsonify(calculate_gst(data["amount"]))

@app.route("/stock", methods=["GET"])
def stock():
    symbol = request.args.get("symbol")
    return jsonify(get_stock_price(symbol))

@app.route("/phone", methods=["POST"])
def phone():
    data = request.get_json()
    return jsonify(phone_control(data["command"]))

@app.route("/voice", methods=["GET"])
def voice():
    return jsonify(listen_voice_command())

@app.route("/add_feature", methods=["POST"])
def add_feature():
    data = request.get_json()
    add_new_feature(data["feature"])
    return jsonify({"status": "Success", "message": "Feature Added Successfully!"})

# ✅ Start Flask Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
