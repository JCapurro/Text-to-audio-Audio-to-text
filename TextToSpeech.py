from gtts import gTTS

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
import os,PyPDF2
import speech_recognition as sr
import pyaudio

def language_selection():
    language="a"
    print("\nSelect:\n\t1.English\n\t2.Spanish\n\t3.Russian\n\t4.Chinese")
    while language =="a":
        select = input()
        if select == '1':
            language='en'
        elif select=='2':
            language='es'
        elif select=='3':
            language='ru'
        elif select=='4':
            language='zh'
        else:
            print("\nIncorrect option.\n\n\t Select again: \n\t\t1.English\n\t\t2.Spanish\n\t\t3.Russian\n\t\t4.Chinese")
    return language

def TextToSpeech(myText):
    language = language_selection()
    os.system("cls")
    output= gTTS(text=myText,lang=language,slow=False)
    name=input("Introduce the name of the file: ")
    os.system("cls")
    print("Wait until the file is ready to listen.This could take some minutes ")
    output.save(name+'.mp3')
    os.startfile(name+'.mp3')

def SpeechToText(r):
    with sr.Microphone() as source:
        #duration=int(input("Introduce the time you want to speak: "))
        print("Recognizing...")
        r.adjust_for_ambient_noise(source)
        audio_data = r.listen(source)
        text = r.recognize_google(audio_data,language='es-ES')
    return text

Tk().withdraw()
os.system("cls")
active=True
print("\nSelect a program:\n\t1.Text to Audio\n\t2.Audio to Text\n\t3.Exit")
while active:
    program=input()
    os.system("cls")
    if program=='1':
        status=True
        print("\nSelect:\n\t1.From PDF\n\t2.From input")
        opt=input()
        os.system("cls")
        if opt=='1':
            os.system("cls")
            myText=''
            pdfFileObject = open(askopenfilename(), 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
            count = pdfReader.numPages
            for i in range(count):
                page = pdfReader.getPage(i)
                myText+=page.extractText()
            TextToSpeech(myText)
        elif opt=='2':
            os.system("cls")
            myText=input("Introduce the text: ")
            TextToSpeech(myText)
        else:
            print("\nIncorrect option.\n\n\t Select again: \n\t1.From PDF\n\t2.From input ")

    elif program=='2':
        r=sr.Recognizer()
        text=SpeechToText(r)
        txt_file=open('output.txt','w')
        txt_file.write(text)
        txt_file.close()
        os.system('start output.txt')
        print(text)
    elif program=='3':
        active=False
        print('Closing the app...')
    else:
        print("Incorrect option. Select again: \n\t1.Text to Audio\n\t2.Audio to Text\n\t3.Exit")
