# Import libraries
import streamlit as st

# Add a title
st.title("Anonymous Suggestion Box")

# Initialize a list so we can store suggestions
# This is a temp list, and only works while the app is running
suggestions = []  #  [] represents an empty list

# Create a text area where the user can type their suggestion
user_input = st.text_area("What is your suggestion", height=150)

# Create a submit button
if st.button("Submit"):
    # When the user has typed something and hits submit
    if user_input.strip() != "":
        suggestions.append(user_input) # Save the suggestion to the list
        st.success("Thank you for the suggestion!")
    else:
        st.warning("Please entere a suggestion before submitting.")

# Show all previous suggestions
st.header("Previous Suggestions:")

if suggestions:
    for idx, suggestion in enumerate(suggestions, start=1):
        st.write(f"{idx}. {suggestion}")
else:
    st.write("No suggestions yet.  Be the first!")
