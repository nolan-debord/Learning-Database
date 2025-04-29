# Import the Streamlit Library
import streamlit as st

# Set the title a the top of the app
st.title("My First Streamlit App!")

# Line of text below the title
st.write("Hello, welcome to my very first app!")

# Create a text input field where the user can type something
name = st.text_input("What's your name?")

# Add a dropdown menu
mood = st.selectbox(
    "How are you feeling today?",
    ("Happy", "Sad", "Excited", "Tired", "Angry")
)

# Add a Slider
rating = st.slider("Rate your day from 1-10", 1, 10, 5)  # in this case 5 is where the slider starts

# Add a button
if st.button("Submit"):
    st.write(f"Hello {name}! You're feeling {mood} and rated your day today as a {rating}/10.")

# Add an image
st.image("https://picsum.photos/400/300", caption="Here's a radnom image!")

# Add a Progress bar
import time
progress = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)

st.success("Done Loading!")  # Adds a green checkmark box
