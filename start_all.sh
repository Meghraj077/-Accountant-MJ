#!/bin/bash

echo "🔹 Accountant-MJ: Initializing Setup..."

# ✅ Update & Install Dependencies
apt update && apt upgrade -y
pkg install python git nano curl -y
pip install --upgrade pip
pip install flask pandas numpy speechrecognition openai requests

# ✅ Stop Any Running Instances
pkill -f tax_api.py
pkill -f voice_recognition.py
pkill -f main.py
pkill -f ocr_service.py
pkill -f finance_tracker.py
pkill -f chatbot.py

# ✅ Start Flask API (tax_api.py)
echo "🔹 Starting Tax API..."
nohup python tax_api.py > tax_api.log 2>&1 &

# ✅ Start Voice Recognition (voice_recognition.py)
echo "🔹 Starting Voice Recognition..."
nohup python voice_recognition.py > voice.log 2>&1 &

# ✅ Start Main AI System (main.py)
echo "🔹 Starting Accountant-MJ AI..."
nohup python main.py > main.log 2>&1 &

# ✅ Start OCR Service (ocr_service.py)
echo "🔹 Starting OCR Service..."
nohup python ocr_service.py > ocr.log 2>&1 &

# ✅ Start Finance Tracker (finance_tracker.py)
echo "🔹 Starting Finance Tracker..."
nohup python finance_tracker.py > finance.log 2>&1 &

# ✅ Start AI Chatbot (chatbot.py)
echo "🔹 Starting AI Chatbot..."
nohup python chatbot.py > chatbot.log 2>&1 &

echo "✅ Accountant-MJ is now Running!"

# ✅ Voice Command Listener (Auto Stop Feature)
echo "🎤 Voice Command Listening for 'STOP'..."
while true; do
    command=$(python3 voice_recognition.py)  # Voice Command Detection
    if [[ "$command" == "STOP" ]]; then
        echo "🛑 Voice Command Detected: Stopping all services..."
        pkill -f tax_api.py
        pkill -f voice_recognition.py
        pkill -f main.py
        pkill -f ocr_service.py
        pkill -f finance_tracker.py
        pkill -f chatbot.py
        echo "✅ All services stopped!"
        exit 0
    fi
done
