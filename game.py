import streamlit as st
import random

<<<<<<< HEAD

=======
>>>>>>> 99c6939fbcb92e4ac11a947eada576fdbb9e6467
def guessing_game():
    st.title("Number Guessing Game")
    st.write("Welcome to the Number Guessing Game!")

    
    if 'number_to_guess' not in st.session_state:
        st.session_state.number_to_guess = random.randint(1, 100)
        st.session_state.attempts = 0

<<<<<<< HEAD
    
    st.write(f"Attempts: {st.session_state.attempts}")

    
    guess = st.number_input("Guess a number between 1 and 100:", min_value=1, max_value=100, step=1)

    
=======
   
    st.write(f"Attempts: {st.session_state.attempts}")

   
    guess = st.number_input("Guess a number between 1 and 100:", min_value=1, max_value=100, step=1)

   
>>>>>>> 99c6939fbcb92e4ac11a947eada576fdbb9e6467
    if st.button("Check Guess"):
        st.session_state.attempts += 1
        if guess < st.session_state.number_to_guess:
            st.write("Too low! Try again.")
        elif guess > st.session_state.number_to_guess:
            st.write("Too high! Try again.")
        else:
            st.write(f"Congratulations! You guessed the number {st.session_state.number_to_guess} in {st.session_state.attempts} attempts!")
<<<<<<< HEAD
    
=======
           
>>>>>>> 99c6939fbcb92e4ac11a947eada576fdbb9e6467
            st.session_state.number_to_guess = random.randint(1, 100)
            st.session_state.attempts = 0


if __name__ == "_main_":
    guessing_game()
