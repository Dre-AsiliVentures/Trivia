"""
Joseph Prince: There is Hope in the Grace of God | Praise on TBN
"""
import streamlit as st
import pandas as pd
import numpy as np
import random

st.write(" Trivia: Sermon by Joseph Prince: There is Hope in the Grace of God")
# Load the Excel file
url = "https://asiliventures.com/wp-content/uploads/2023/06/JosephPrince_There_is_Hope_in_God.xlsx"
df = pd.read_excel(url)

# Replace nan values in options with empty string
df.fillna("", inplace=True)

# Initialize the score
total_score = 0
# Display each question
for index, row in df.iterrows():
    question = row['Question']
    if pd.isnull(question) or question.strip() == "":
        chapter = row['Chapter']
        st.write(f"**Chapter {chapter}:**")
    else:
        #question_number = index  # Adjust question number
        st.write(f"**Question {index}:** {question}")
        # Randomize the order of options
        options = [row['Option A'], row['Option B'], row['Option C'], row['Option D']]
        random.shuffle(options)

        # Display randomized options
        option = st.radio("Select an option:", options=options,key=f"options_{index}",index=options.index(selected_options[index]))

        # Display hints
        if st.button("Word Hint", key=f"word_hint_{index}"):
            st.write(f"Word Hint: {row['Word Hint']}")
        if st.button("Time Hint", key=f"time_hint_{index}"):
            st.write(f"Time Hint: {row['Time Hint']}")

        # Check answer
        if st.button("Check Answer", key=f"check_answer_{index}"):
            if option == row['Correct Answer']:
                st.write("Correct!")
                total_score += 1
            else:
                st.write("Incorrect.")
                total_score=total_score
            option[index]=option

    st.write("---")

# Display total quiz score
st.write(f"Total Score: {total_score}/{len(df)}")

