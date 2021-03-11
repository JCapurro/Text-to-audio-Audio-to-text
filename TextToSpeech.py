from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
import PyPDF2,os,pyaudio,subprocess
from gtts import gTTS
import speech_recognition as sr

def language_speech():
    language="a"
    print("\nSelect:\n\t1.English\n\t2.Spanish\n\t3.Russian\n\t4.Chinese")
    while language =="a":
        select = input()
        if select == '1':
            language='en-EN'
        elif select=='2':
            language='es-ES'
        elif select=='3':
            language='ru-RU'
        elif select=='4':
            language='zh-ZH'
        else:
            print("\nIncorrect option.\n\n\t Select again: \n\t\t1.English\n\t\t2.Spanish\n\t\t3.Russian\n\t\t4.Chinese")
    return language

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
    os.system("cls")
    print("Wait until the file is ready to listen.This could take some minutes ")
    output.save('output.mp3')
    os.startfile('output.mp3')

def SpeechToText(r):
    lang=language_speech()
    with sr.Microphone() as source:
        os.system('cls')
        print("Recognizing...")
        r.adjust_for_ambient_noise(source)
        audio_data = r.listen(source)
        text = r.recognize_google(audio_data,language=lang)
    return text

Tk().withdraw()
os.system("cls")
active=True
while active:
    print("\nSelect a program:\n\t1.Text to Audio\n\t2.Audio to Text\n\t3.Exit")
    program=input()
    os.system("cls")
    while program=='1':
        print("\nSelect:\n\t1.From PDF\n\t2.From input\n\t3.Back")
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
        elif opt=='3':
            program='0'

    while program=='2':
        print("\nSelect:\n\t1.From Voice\n\t2.From .wav\n\t3.Back")
        opt=input()
        os.system("cls")
        if opt=='1':
            r=sr.Recognizer()
            text=SpeechToText(r)
            txt_file=open('output.txt','w')
            txt_file.write(text)
            txt_file.close()
            os.system('start output.txt')
            os.system('cls')
            os.system
        elif opt=='2':
            os.system('cls')
            file=askopenfilename()
            r=sr.Recognizer()
            with sr.AudioFile(file) as source:
                print("Wait until the file is ready to listen.This could take some minutes ")
                audio_data = r.record(source)
                text = r.recognize_google(audio_data)
            txt_file=open('output.txt','w')
            txt_file.write(text)
            txt_file.close()
            os.system('start output.txt')
            os.system('cls')
        elif opt=='3':
            program='0'


    if program=='3':
        active=False
        print('Closing the app...')

