import streamlit as st
import random

# Function to generate a random number and start the game
def guessing_game():
    st.title("Number Guessing Game")
    st.write("Welcome to the Number Guessing Game!")

    # Store the random number in session state if it's not already set
    if 'number_to_guess' not in st.session_state:
        st.session_state.number_to_guess = random.randint(1, 100)
        st.session_state.attempts = 0

    # Display the number of attempts
    st.write(f"Attempts: {st.session_state.attempts}")

    # Get user input for their guess
    guess = st.number_input("Guess a number between 1 and 100:", min_value=1, max_value=100, step=1)

    # Button to check the guess
    if st.button("Check Guess"):
        st.session_state.attempts += 1
        if guess < st.session_state.number_to_guess:
            st.write("Too low! Try again.")
        elif guess > st.session_state.number_to_guess:
            st.write("Too high! Try again.")
        else:
            st.write(f"Congratulations! You guessed the number {st.session_state.number_to_guess} in {st.session_state.attempts} attempts!")
            # Reset the game after a correct guess
            st.session_state.number_to_guess = random.randint(1, 100)
            st.session_state.attempts = 0

# Start the game
if __name__ == "__main__":
    guessing_game()