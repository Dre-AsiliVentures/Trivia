"""
Joseph Prince: There is Hope in the Grace of God | Praise on TBN
"""

st.write(" Trivia: Sermon by Joseph Prince: There is Hope in the Grace of God")
import streamlit as st
import pandas as pd
import numpy as np

# Load the Excel file
url = "https://asiliventures.com/wp-content/uploads/2023/06/JosephPrince_There_is_Hope_in_God.xlsx"
df = pd.read_excel(url)

# Replace nan values in options with empty string
df.fillna("", inplace=True)

# Initialize the score
total_score = 0

# Display each question
for index, row in df.iterrows():
    st.write(f"**Question {index+1}:** {row['Question']}")

    # Display options
    option = st.radio("Select an option:", options=[row['Option A'], row['Option B'], row['Option C'], row['Option D']])

    # Display hints
    if st.button("Word Hint", key=f"word_hint_{index}"):
        st.write(f"Word Hint: {row['Word']}")
    if st.button("Time Hint", key=f"time_hint_{index}"):
        st.write(f"Time Hint: {row['Time Hint']}")

    # Check answer
    if st.button("Check Answer", key=f"check_answer_{index}"):
        if option == row['Correct Answer']:
            st.write("Correct!")
            total_score += 1
        else:
            st.write("Incorrect.")

    st.write("---")

# Display total quiz score
st.write(f"Total Score: {total_score}/{len(df)}")


