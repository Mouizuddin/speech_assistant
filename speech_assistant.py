import speech_recognition as speech
from datetime import date, datetime
import webbrowser

main = speech.Recognizer()
import time
import os
import playsound
import random
from gtts import gTTS

'''
note the voice and print the voice data
'''


def audio(default_ask=False):
    with speech.Microphone() as microphone:
        if default_ask:
            print(default_ask)
        #         print("Talk user!")
        audio = main.listen(microphone)
    audio_data = " "
    try:
        audio_data = main.recognize_google(audio)
    #             print(audio_data)
    except speech.UnknownValueError as unknown:
        print(f'unknown > {unknown}')
    except speech.RequestError as error:
        print(f'Unknown error > {error}')
    except KeyboardInterrupt as keybord:
        print(f'Taking to much time {Keyboard}')
    return audio_data


def takl_back(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    #     ran = random.randint(1,1000000)
    audio_file = 'mouiz' + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def responces(record_audio):
    if 'what is your name'.lower() in record_audio:
        print("My name is mouiz")
    if "time now".lower() in record_audio:
        current_time = now.strftime("%H:%M")
        print("Current Time =", current_time)

    if "today date" in record_audio:
        today = date.today()
        print("Today's date:", today)

    if 'find' in record_audio:
        find = record_audio("What to find?")
        url = 'https://www.google.com/search?q=' + find
        webbrowser.get().open_new_tab(url)
        print('Found result >>' + find)
    if 'exit' in record_audio:
        exit()


time.sleep(1)
print("Talk User!")
while True:
    record_audio = audio()
    #     print(record_audio)
    responce = responces(record_audio)