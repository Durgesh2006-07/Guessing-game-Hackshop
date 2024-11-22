import streamlit as st
import random


def guessing_game():
    st.title("Number Guessing Game")
    st.write("Welcome to the Number Guessing Game!")

    
    if 'number_to_guess' not in st.session_state:
        st.session_state.number_to_guess = random.randint(1, 100)
        st.session_state.attempts = 0

    
    st.write(f"Attempts: {st.session_state.attempts}")

    
    guess = st.number_input("Guess a number between 1 and 100:", min_value=1, max_value=100, step=1)

    
    if st.button("Check Guess"):
        st.session_state.attempts += 1
        if guess < st.session_state.number_to_guess:
            st.write("Too low! Try again.")
        elif guess > st.session_state.number_to_guess:
            st.write("Too high! Try again.")
        else:
            st.write(f"Congratulations! You guessed the number {st.session_state.number_to_guess} in {st.session_state.attempts} attempts!")
    
            st.session_state.number_to_guess = random.randint(1, 100)
            st.session_state.attempts = 0


if __name__ == "_main_":
    guessing_game()