# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import speech_recognition as sr
import webbrowser as wb
from googletrans import Translator
from gtts import gTTS
import os
from pocketsphinx import pocketsphinx, Jsgf, FsgModel
from playsound import playsound


def choose_Language(name,srcLanguage,audio):
    s1 = sr.Recognizer()
    trans = Translator()

    if name in s1.recognize_google(audio):
        with sr.Microphone() as source:
            print('Please speak')
            audio_data = s1.record(source, duration=5)
            text = s1.recognize_google(audio_data)
            print('Before Translation '+text)
            text_trn = trans.translate(text, dest='en', src=srcLanguage)
            print(text_trn.pronunciation)
            tts= gTTS(text_trn.pronunciation)
            tts.save("trs.mp3")
            playsound('trs.mp3')

if __name__ == '__main__':

    s1 = sr.Recognizer()
    s2 = sr.Recognizer()
    s3 = sr.Recognizer()

    with sr.Microphone() as source:
        print('Choose Your Language[Spanish]')
        print('speak now')
        audio = s3.listen(source)
        print(s1.recognize_google(audio))

    if 'Spanish':
      choose_Language('Spanish','es',audio)

    if 'English':
      choose_Language('Spanish','en',audio)

    # elif 'german':
    #   choose_Language('Spanish','de')
    #
    # elif 'Spanish':
    #   choose_Language('Spanish','es')





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
