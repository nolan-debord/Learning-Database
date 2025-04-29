import streamlit as st

# Add a title
st.title("Page 2 - Fun Stats")

# number slider
number = st.slider("Pick a number", 1, 100)

# Respond to the number picked
st.write(f"You picked: {number}")

# add a bar chart of this number
st.bar_chart({"Numbers": [number, number * 2, number * 3]})