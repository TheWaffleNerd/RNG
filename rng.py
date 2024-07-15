import streamlit as st
import random

num1 = random.randrange(1, 5)
num2 = random.randrange(5, 8)

st.title("Welcome to the Random Number Guessing Game")

txt_guess1 = int(st.text_input("Enter a number between 1 to 4: ", 1))
txt_guess2 = int(st.text_input("Enter a number between 5 to 7: ", 5))

btn_guess = st.button("Submit guess")
if btn_guess:
    if (txt_guess1 == num1 or txt_guess2 == num2):
        st.write("You have guessed the correct number")
        st.balloons();
    else:
        html_str1 = f""" <h1 style ="font-size = 16px; text_align: left; color: #FF4433;">Sorry, please try again</h1> """
        st.markdown(html_str1, unsafe_allow_html=True)

st.write("The correct number are: ", num1, "and", num2)

with st.expander("Help"):
    st.write("To play the game, please enter your guesses in the textboxes. Press submit guess when you are ready to guess.")