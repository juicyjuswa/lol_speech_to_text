# Record-From-The-Mic

# Save-That-As-A-.wav

# Speech-To-Text-On-That-.wav

#Type-That-In-League-without-Messing-It-Up

# Import-Necessary-Modules
import speech_recognition as sr
import numpy as np
import sounddevice as sd
import wave
import keyboard
import pyautogui as pag
from time import sleep

import speech_recognition as sr
import numpy as np
import sounddevice as sd
import wave

import keyboard
import pyautogui as pag
from time import sleep

#File-Name-To-Save
FILE_NAME = './lol_speech_to_text.wav'

#Recording-Length-(seconds)
wave_length = 4

# Sampling-Frequency
sample_rate = 16_000

while True:
    keyboard.wait('v')
    print("RECORDING ***")
    # Start-Recording 
    data = sd.rec(int(wave_length * sample_rate), sample_rate, channels=1)
    sd.wait()
   
    # Normalize
    data = data / data.max() * np.iinfo(np.int16).max
   
    # Float-To-Int
    data = data.astype(np.int16)
   
    #Save-File
    with wave.open(FILE_NAME, mode='wb') as wb:
        # Monaural
        wb.setnchannels(1)
        # 16bit=2byte
        wb.setsampwidth(2)
        wb.setframerate(sample_rate)
        # Convert-To-Byte-String
        wb.writeframes(data.tobytes())
    #File-Name-To-Save
    filename = "lol_speech_to_text.wav"
    r = sr.Recognizer()
   
    with sr.AudioFile(filename) as source:
        # Listen-For-The-Data
        audio_data = r.record(source)
        # Convert-From-Speech-To-Text)
        text = r.recognize_google(audio_data)
        print(text)

    keyboard.press_and_release('enter')
    sleep(0.01)
    pag.write(text)
    keyboard.press_and_release('enter')