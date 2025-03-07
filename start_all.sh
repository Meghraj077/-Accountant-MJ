#!/bin/bash

echo "🔹 Accountant-MJ: Initializing Setup..."

# ✅ Update & Install Dependencies
apt update && apt upgrade -y
pkg install python git nano curl termux-api -y
pip install --upgrade pip
pip install flask pandas numpy speechrecognition openai requests pytesseract pdf2image python-docx gtts

# ✅ Stop Any Running Instances
pkill -f tax_api.py
pkill -f voice_recognition.py
pkill -f main.py
pkill -f ocr_service.py
pkill -f finance_tracker.py
pkill -f chatbot.py
pkill -f fraud_detection.py
pkill -f document_management.py
pkill -f personal_assistant.py
pkill -f finance_advisor.py
pkill -f mobile_control.py
pkill -f voice_cloning.py

# ✅ Start Services
echo "🔹 Starting Tax API..."
nohup python tax_api.py > tax_api.log 2>&1 &

echo "🔹 Starting Voice Recognition..."
nohup python voice_recognition.py > voice.log 2>&1 &

echo "🔹 Starting Main AI System..."
nohup python main.py > main.log 2>&1 &

echo "🔹 Starting OCR Service..."
nohup python ocr_service.py > ocr.log 2>&1 &

echo "🔹 Starting Finance Tracker..."
nohup python finance_tracker.py > finance.log 2>&1 &

echo "🔹 Starting AI Chatbot..."
nohup python chatbot.py > chatbot.log 2>&1 &

echo "🔹 Starting AI Fraud Detection..."
nohup python fraud_detection.py > fraud.log 2>&1 &

echo "🔹 Starting AI Document Management..."
nohup python document_management.py > doc_mgmt.log 2>&1 &

echo "🔹 Starting AI Personal Assistant..."
nohup python personal_assistant.py > assistant.log 2>&1 &

echo "🔹 Starting AI Finance Advisor..."
nohup python finance_advisor.py > finance_ai.log 2>&1 &

echo "🔹 Starting AI Mobile Control..."
nohup python mobile_control.py > mobile_control.log 2>&1 &

echo "🔹 Starting AI Voice Cloning..."
nohup python voice_cloning.py > voice_clone.log 2>&1 &

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
        pkill -f fraud_detection.py
        pkill -f document_management.py
        pkill -f personal_assistant.py
        pkill -f finance_advisor.py
        pkill -f mobile_control.py
        pkill -f voice_cloning.py
        echo "✅ All services stopped!"
        exit 0
    fi
done
