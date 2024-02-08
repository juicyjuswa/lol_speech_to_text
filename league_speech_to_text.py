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

FILE_NAME = './lol_speech_to_text.wav'
wave_length = 4
sample_rate = 16_000

while True:
    keyboard.wait('v')
    print("RECORDING ***")
    data = sd.rec(int(wave_length * sample_rate), sample_rate, channels=1)
    sd.wait()
    data = data / data.max() * np.iinfo(np.int16).max
    data = data.astype(np.int16)
   
    with wave.open(FILE_NAME, mode='wb') as wb:
        wb.setnchannels(1)
        wb.setsampwidth(2)
        wb.setframerate(sample_rate)
        wb.writeframes(data.tobytes())
    filename = "lol_speech_to_text.wav"
    r = sr.Recognizer()
   
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        print(text)

    keyboard.press_and_release('enter')
    sleep(0.01)
    pag.write(text)
    keyboard.press_and_release('enter')

    # note you need internet for this to work
    #STEPS TO USE
    # 1.)OPEN LEAGUE OF LEGENDS AND FIND A MATCH
    # 2.)WHILE INSDE THE MATCH, PRESS V TO INITIATE "keyboard.wait('v')" AND RUN THE CODE
    # 3.) SAY ANY COMMS THROUGH YOUR MIC THAT YOU WOULD LIKE YOUR TEAMMATES TO KNOW
    # 4.) AFTER TALKING, PRESS ENTER TWICE, CONSECUTIVELY
    # 5.) WHAT YOU TOLD THE MIC WOULD BE CONVERTED TO TEXT AND AUTOMATICALLY BE TYPED THROUGH IN GAME CHAT WHILE PLAYING
