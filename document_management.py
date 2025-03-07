import os
import pytesseract
from pdf2image import convert_from_path
import docx
import speech_recognition as sr

def extract_text_from_pdf(pdf_path):
    """ PDF से टेक्स्ट निकालें """
    images = convert_from_path(pdf_path)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)
    return text

def create_word_doc(text, file_name="output.docx"):
    """ Word File Generate करें """
    doc = docx.Document()
    doc.add_paragraph(text)
    doc.save(file_name)
    return f"Word File Saved: {file_name}"

def document_voice_command():
    """ Voice से Document Processing करें """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Document Command सुन रहा हूँ...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()

        if "extract text" in command:
            pdf_path = command.split("from")[-1].strip()
            text = extract_text_from_pdf(pdf_path)
            print(f"Extracted Text: {text}")

        elif "create word file" in command:
            text = input("Enter Text: ")
            print(create_word_doc(text))

        else:
            print("Unknown document command!")

    except:
        print("Sorry, समझ नहीं पाया!")

if __name__ == "__main__":
    document_voice_command()
