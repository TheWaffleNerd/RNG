import streamlit as st
import random

counter = 0
num = random.randrange(1, 10)

st.title("Welcome to the Random Number Guessing Game")

txt_guess = int(st.text_input("Enter a number between 1 to 10: ", 1))

btn_restart = st.button("Reset")

btn_guess = st.button("Submit guess")
if btn_guess:
    if txt_guess == num:
        st.write("You have guessed the correct number")
        st.balloons();
    else:
        html_str1 = f""" <h1 style ="text_align: left; color: #FF4433;">Sorry, please try again</h1> """
        st.markdown(html_str1, unsafe_allow_html=True)
        counter = counter + 1


btn_reveal = st.button("Reveal answer")
if btn_reveal:
    st.write("The correct number is: ", num)
