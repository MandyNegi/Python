# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import speech_recognition as sr
import webbrowser as wb
from googletrans import Translator
from gtts import gTTS
import os
from playsound import playsound



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
      # Press Ctrl+F8 to toggle the breakpoint.
    s1 = sr.Recognizer()
    s2 = sr.Recognizer()
    s3 = sr.Recognizer()
    trans = Translator()
    # text_trn = trans.translate('Mitä sinä teet')
    # print('After Translation ' + text_trn)

    with sr.Microphone() as source:
        print('search something')
        print('speak now')
        audio = s3.listen(source)
        print(audio)

    if 'youtube' in s2.recognize_google(audio):
        s2 = sr.Recognizer()
        url = 'https://www.youtube.com/'
        with sr.Microphone() as source:
            print('search your query')
            audio = s2.listen(source)
            try:
                get = s2.recognize_google(audio)
                print(get)
                wb.get().open_new(url+get)
            except sr.UnknownValueError:
                print('error')
            except sr.RequestError as e:
                print('failed'.format(e))

    if 'type' in s1.recognize_google(audio):
        with sr.Microphone() as source:
            # listen for the data (load audio to memory)
            print('speak your text')
            audio_data = s1.record(source, duration=5)
            # recognize (convert from speech to text)
            # text = s1.recognize_google(audio_data, language="es-ES")
            text = s1.recognize_google(audio_data)
            print('Before Translation '+text)
            text_trn = trans.translate(text, dest='hi')
            print(text_trn.pronunciation)
            tts= gTTS(text_trn.pronunciation)
            tts.save("trs.mp3")
            playsound('trs.mp3')
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
