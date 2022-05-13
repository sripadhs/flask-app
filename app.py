import streamlit as sl
import pyttsx3
speaker=pyttsx3.init()
sl.title('Hello!')

inp=sl.text_input('Enter your name:')
if sl.button('say hello!'):
    sl.write('hello'+' '+inp)
    speaker.say('hello'+inp)
speaker.runAndWait()