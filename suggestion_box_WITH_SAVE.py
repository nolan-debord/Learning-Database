# Import libraries
import streamlit as st
import os # to check if file exists

# Add a title
st.title("Anonymous Suggestion Box")

# Set filename for saving suggestions
FILENAME = "suggestions.txt"

# Helper function: Load suggestions from file
def load_suggestions():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    else:
        return []

# Helper function: Save a new suggestion to file
def save_suggestion(text):
    with open(FILENAME, "a") as file:
        file.write(text + "\n")
                   
# load the suggestions                   
suggestions = load_suggestions() 

# Create a text area where the user can type their suggestion
user_input = st.text_area("What is your suggestion", height=150)

# Create a submit button
if st.button("Submit"):
    # When the user has typed something and hits submit
    if user_input.strip() != "":
        save_suggestion(user_input) # Save the suggestion
        st.success("Thank you for the suggestion!")
        st.rerun() # Refresh the page to show new suggestions
    else:
        st.warning("Please entere a suggestion before submitting.")

# Show all previous suggestions
st.header("Previous Suggestions:")

if suggestions:
    for idx, suggestion in enumerate(suggestions, start=1):
        st.write(f"{idx}. {suggestion}")
else:
    st.write("No suggestions yet.  Be the first!")