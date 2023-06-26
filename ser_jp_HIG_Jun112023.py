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
total_score = 0
correct_answers = []
incorrect_answers = []
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
        if st.button("Check Answer", key=f"check_answer_{index}"):
            if option == row['Correct Answer']:
                st.write("Correct!")
                total_score += 1
                correct_answers.append(question_number)
                #total_score=len(correct_answers)
            else:
                st.write("Incorrect.")
                total_score=total_score
                incorrect_answers.append(question_number)
                #total_score=len(correct_answers)
            

    st.write("---")
# Display total quiz score
#total_score=len(correct_answers)
st.write(f"Total Score: {total_score}/{len(df)}")
# Display questions answered correctly
# if correct_answers:
#     st.write("Questions Answered Correctly:")
#     for question_number in correct_answers:
#         st.write(f"Question {question_number}")
# else:
#     st.write("No questions answered correctly.")

# # Display questions answered incorrectly
# if incorrect_answers:
#     st.write("Questions Answered Incorrectly:")
#     for question_number in incorrect_answers:
#         st.write(f"Question {question_number}")
# else:
#     st.write("No questions answered incorrectly.")



