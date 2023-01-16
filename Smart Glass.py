import cv2
from PIL import Image
from pytesseract import pytesseract
import pyttsx3
from logging import exception
import speech_recognition as sr
import webbrowser

def tesseract():
    path_to_tesseract=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    Imagepath='test1.jpg'
    pytesseract.tesseract_cmd=path_to_tesseract
    answer=pytesseract.image_to_string(Image.open(Imagepath))
    print(answer[:-1])
    
   # text_speech.say(" Hey Hello")
    text_speech.say(answer)
    text_speech.say("Thank you")
    text_speech.runAndWait()



text_speech=pyttsx3.init()
try:
    text_speech.say("Opening camera please wait...")
    text_speech.runAndWait()
    a =cv2.VideoCapture(0)
    while True:
        _, image = a.read()
        cv2.imshow('Text detection', image)
        if cv2.waitKey(1)& 0xFF==ord('s'):
            cv2.imwrite("test1.jpg",image)
            break
    a.release()
    cv2.destroyAllWindows()
    tesseract()

except Exception as e:
    text_speech.say("I don't recognize you")
    text_speech.runAndWait()
    print(str(e))