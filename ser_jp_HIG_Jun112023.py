"""
Joseph Prince: There is Hope in the Grace of God | Praise on TBN
"""
import streamlit as st
import pandas as pd
import numpy as np


st.write(" Trivia: Sermon by Joseph Prince: There is Hope in the Grace of God")
# Load the Excel file
url = "https://asiliventures.com/wp-content/uploads/2023/06/JosephPrince_There_is_Hope_in_God.xlsx"
df = pd.read_excel(url)

# Replace nan values in options with empty string
df.fillna("", inplace=True)

# Initialize the score and selected options list
# Initialize the score and selected options list
if "total_score" not in st.session_state:
    st.session_state["total_score"] = 0
question_results = {}
# Display each question
for index, row in df.iterrows():
    question = row['Question']
    if pd.isnull(question) or question.strip() == "":
        chapter = row['Chapter']
        st.write(f"**Chapter {chapter}:**")
    else:
        question_number = index  # Adjust question number
        st.write(f"**Question {index}:** {question}")
        # Display options
        option = st.radio("Select an option:", options=[row['Option A'], row['Option B'], row['Option C'], row['Option D']])

        # Display hints
        if st.button("Word Hint", key=f"word_hint_{index}"):
            st.write(f"Word Hint: {row['Word Hint']}")
        if st.button("Time Hint", key=f"time_hint_{index}"):
            st.write(f"Time Hint: {row['Time Hint']}")

        # Check answer
        check_answer = st.button("Check Answer", key=f"check_answer_{index}")

        question_result_key = f"result_{index}"
        if question_result_key not in st.session_state:
            st.session_state[question_result_key] = None

        if check_answer:
            if option == row['Correct Answer']:
                st.write("Correct!")
                st.session_state[question_result_key] = "Correct"
                st.session_state["total_score"] += 1
            else:
                st.write("Incorrect.")
                st.session_state[question_result_key] = "Incorrect"
            

    st.write("---")
# Display total quiz score
st.write(f"Total Score: {st.session_state['total_score']}/{len(df)}")
# Display questions answered correctly
correct_answers = [i + 1 for i, result in enumerate(st.session_state.values()) if result == "Correct"]
if correct_answers:
    st.write("Questions Answered Correctly:")
    for question_number in correct_answers:
        st.write(f"Question {question_number}")
else:
    st.write("No questions answered correctly.")

# Display questions answered incorrectly
incorrect_answers = [i + 1 for i, result in enumerate(st.session_state.values()) if result == "Incorrect"]
if incorrect_answers:
    st.write("Questions Answered Incorrectly:")
    for question_number in incorrect_answers:
        st.write(f"Question {question_number}")
else:
    st.write("No questions answered incorrectly.")








