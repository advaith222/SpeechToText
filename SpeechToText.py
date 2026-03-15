import speech_recognition as sr
import os
import threading
from mtranslate import translate
from colorama import Fore,Style,init
init(autoreset=True)

def print_loop():
    while True:
        print(Fore.RED +  "Listening...",end="",flush=True)
        print(Style.RESET_ALL,end="",flush=True)

def Translate_tamil_to_english(text):
    english_text= translate(text,"en-us")
    return english_text

def Speech_To_Text_Python():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold= True
    recognizer.energy_threshold= 300
    recognizer.dynamic_energy_adjustment_damping=0.15
    recognizer.dynamic_energy_ratio=1.5
    recognizer.pause_threshold=0.8
    recognizer.operation_timeout=None
    recognizer.pause_threshold=0.8
    recognizer.non_speaking_duration=0.5

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.RED +  "Listening...",end="",flush=True)
            try:
                audio=recognizer.listen(source,timeout=None)
                print("\r"+Fore.BLUE+"Recognising...",end="",flush=True)
                recognizer_text=recognizer.recognize_google(audio,language="ta-IN").lower()
                if recognizer_text:
                    trans_text=Translate_tamil_to_english(recognizer_text)
                    print("\r"+ Fore.GREEN+ "Advaith: " + trans_text)
            
            except sr.UnknownValueError:
                print("\r",end="",flush=True)


        stt_thread=threading.Thread(target=Speech_To_Text_Python)
        print_thread=threading.Thread(target=print_loop)
        stt_thread.start()
        print_loop.start()
        stt_thread.join()
        print_loop.join()

Speech_To_Text_Python()




