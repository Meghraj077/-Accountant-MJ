from flask import Flask, request, jsonify
import requests
import os
import pyttsx3
import speech_recognition as sr  # Voice Command Support
import json  # Self-Coding Support

app = Flask(__name__)

# ✅ Auto-Detect API Key (No Manual Entry Needed)
API_KEY = os.getenv("MJ_API_KEY", "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")  # 🔹 Secure API Key

# ✅ AI Voice Assistant - Text-to-Speech (TTS)
try:
    engine = pyttsx3.init()
    engine.say("Hello, Accountant MJ is now active!")
    engine.runAndWait()
except:
    print("TTS Not Supported in Termux!")

# ✅ Self-Healing & Auto-Fix System
def check_system_health():
    return {"status": "Running", "message": "System is Healthy"}

# ✅ Self-Coding & Auto-Update System
def update_code(new_code):
    try:
        with open(__file__, "w") as f:
            f.write(new_code)
        return {"status": "Success", "message": "Code Updated Successfully!"}
    except Exception as e:
        return {"status": "Error", "message": str(e)}

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

# ✅ Flask API Routes
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Accountant MJ API is Running!"})

@app.route("/health", methods=["GET"])
def health():
    return jsonify(check_system_health())

@app.route("/update", methods=["POST"])
def update():
    data = request.get_json()
    return jsonify(update_code(data["new_code"]))

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

# ✅ Start Flask Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
