# Import the Streamlit Library
import streamlit as st

# Set the title a the top of the app
st.title("My First Streamlit App!")

# Line of text below the title
st.write("Hello, welcome to my very first app!")

# Create a text input field where the user can type something
name = st.text_input("What's your name?")

# If the user has typed something in the input box, display a custom message
if name:
    st.write(f"Nice to meet you, {name}!")

# Create a button labeled "Click Me"
if st.button("Click Me"):
    # When the button is clicked, display a message
    st.write("You clicked the button!")
