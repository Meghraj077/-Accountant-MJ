import os
import json

FRAUD_DB = "fraud_numbers.json"

def load_fraud_numbers():
    """ Fraud Callers की List Load करें """
    if os.path.exists(FRAUD_DB):
        with open(FRAUD_DB, "r") as file:
            return json.load(file)
    return {}

def block_spam_call(number):
    """ Spam Calls Block करें """
    fraud_numbers = load_fraud_numbers()
    if number in fraud_numbers:
        os.system(f"termux-telephony-call -e {number}")  # Call reject करेगा
        return "Fraud Call Blocked!"
    return "Safe Call!"

if __name__ == "__main__":
    print(block_spam_call("1234567890"))
