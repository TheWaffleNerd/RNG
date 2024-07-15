import streamlit as st
import random

st.title("Welcome to the Random Number Guessing Game")


num1
num2

def play_one():
    num1 = random.randrange(1, 5)
    txt_guess1 = int(st.text_input("Enter a number between 1 to 4: ", 1))

def play_two():
    num2 = random.randrange(5, 8)
    txt_guess2 = int(st.text_input("Enter a number between 5 to 7: ", 5))

st.title("Welcome to the Random Number Guessing Game")

btn_select = st.button("Press to guess between 1-4")
if btn_select:
    play_one()

btn_select2 = st.button("Press to guess between 5-7")
if btn_select2:
    play_two()

btn_select3 = st.button("Press to guess for both 1-4 and 5-7")
if btn_select3:
    play_one()
    play_two()

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