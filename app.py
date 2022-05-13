import streamlit as sl

sl.title('Hello!')

inp=sl.text_input('Enter your name:')
if sl.button('say hello!'):
    sl.write('hello'+' '+inp)
    
