import json
import os
import requests
import speech_recognition as sr

# API Keys को सुरक्षित रखें
from dotenv import load_dotenv
load_dotenv()
FINANCE_API_KEY = os.getenv("FINANCE_API_KEY")

def get_stock_price(stock_symbol):
    """ स्टॉक मार्केट डेटा लाने के लिए API Call """
    url = f"https://api.example.com/stocks/{stock_symbol}?apikey={FINANCE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data["price"]

def get_tax_calculation(income):
    """ Income Tax Calculation """
    tax_rate = 0.05 if income < 500000 else 0.2
    return income * tax_rate

def finance_voice_command():
    """ Voice Command से Finance Queries Handle करें """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Finance Command सुन रहा हूँ...")
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        
        if "stock price" in command:
            stock_symbol = command.split("of")[-1].strip().upper()
            price = get_stock_price(stock_symbol)
            print(f"{stock_symbol} का price है: {price}")

        elif "tax calculation" in command:
            income = int(command.split("for")[-1].strip())
            tax = get_tax_calculation(income)
            print(f"Estimated tax: {tax}")

        else:
            print("Unknown finance command!")

    except:
        print("Sorry, समझ नहीं पाया!")

if __name__ == "__main__":
    finance_voice_command()
