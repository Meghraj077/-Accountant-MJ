import os
import json
import hashlib
import getpass

SECURITY_CONFIG = "security_config.json"

def hash_password(password):
    """ पासवर्ड को सुरक्षित तरीके से encrypt करें """
    return hashlib.sha256(password.encode()).hexdigest()

def setup_security():
    """ System के लिए security setup करें """
    if os.path.exists(SECURITY_CONFIG):
        return "Security already set up!"

    password = getpass.getpass("Set Admin Password: ")
    security_data = {"admin_password": hash_password(password)}

    with open(SECURITY_CONFIG, "w") as file:
        json.dump(security_data, file)

    return "Security Setup Completed!"

def authenticate():
    """ System authentication process """
    if not os.path.exists(SECURITY_CONFIG):
        return "Security not set up!"

    password = getpass.getpass("Enter Admin Password: ")

    with open(SECURITY_CONFIG, "r") as file:
        security_data = json.load(file)

    if hash_password(password) == security_data["admin_password"]:
        return "Access Granted!"
    else:
        return "Access Denied!"

def block_unauthorized_access():
    """ Unauthorized Access को detect और block करें """
    print("Checking for unauthorized access...")
    if authenticate() == "Access Denied!":
        print("Warning: Unauthorized access detected!")
        os.system("shutdown -h now")  # Unauthorized access होने पर system बंद कर देगा

if __name__ == "__main__":
    setup_security()
    block_unauthorized_access()
