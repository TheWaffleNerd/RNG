import streamlit as st
import random

@st.cache
def play(flag):
    if flag == 1:
        num1 = random.randrange(1, 5)
        txt_guess1 = int(st.text_input("Enter a number between 1 to 4: ", 1))
    elif flag == 2:
        num2 = random.randrange(5, 8)
        txt_guess2 = int(st.text_input("Enter a number between 5 to 7: ", 5))
    else:
        num1 = random.randrange(1, 5)
        txt_guess1 = int(st.text_input("Enter a number between 1 to 4: ", 1))
        num2 = random.randrange(5, 8)
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

st.title("Welcome to the Random Number Guessing Game")

btn_select = st.button("Press to guess between 1-4")
if btn_select:
    play(1)

btn_select2 = st.button("Press to guess between 5-7")
if btn_select2:
    play(2)

btn_select3 = st.button("Press to guess for both 1-4 and 5-7")
if btn_select3:
    play(3)

with st.expander("Help"):
    st.write("To play the game, please enter your guesses in the textboxes. Press submit guess when you are ready to guess.")