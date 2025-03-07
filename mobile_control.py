import os
import speech_recognition as sr

def open_app(app_name):
    """ Mobile App खोलने का Function """
    os.system(f"termux-open {app_name}")

def send_sms(number, message):
    """ Termux API से SMS भेजें """
    os.system(f"termux-sms-send -n {number} '{message}'")

def mobile_voice_command():
    """ Voice Command से Mobile Control करें """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mobile Command सुन रहा हूँ...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()

        if "open" in command:
            app_name = command.split("open")[-1].strip()
            open_app(app_name)

        elif "send sms" in command:
            parts = command.split("to")
            number = parts[1].split("message")[0].strip()
            message = parts[1].split("message")[-1].strip()
            send_sms(number, message)

        else:
            print("Unknown mobile command!")

    except:
        print("Sorry, समझ नहीं पाया!")

if __name__ == "__main__":
    mobile_voice_command()
