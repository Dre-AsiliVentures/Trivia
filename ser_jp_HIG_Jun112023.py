"""
Joseph Prince: There is Hope in the Grace of God | Praise on TBN
"""
import streamlit as st
import pandas as pd

st.write(" Trivia: Sermon by Joseph Prince: There is Hope in the Grace of God")
# Load the Excel file
df = pd.read_excel('https://asiliventures.com/wp-content/uploads/2023/06/JosephPrince_There_is_Hope_in_God.xlsx')

# Get unique chapters
chapters = df['Chapter'].unique()

# Initialize score
score = 0

# Create a dictionary to store the questions and answers for each chapter
chapter_questions = {}
for i in range(len(df)):
  chapter = df.loc[i, "Chapter"]
  question = df.loc[i, "Question"]
  answer = df.loc[i, "Correct Answer"]
  options = [df.loc[i, "Option A"], df.loc[i, "Option B"], df.loc[i, "Option C"], df.loc[i, "Option D"]]
  chapter_questions[chapter] = {"question": question, "answer": answer, "options": options}

# Create a container for each chapter
for chapter in chapter_questions:
  #st.container(chapter, title="Chapter")
  #st.write(chapter_questions[chapter]["question"])
  #st.section(chapter)
  #st.write(chapter_questions[chapter]["question"])
  #st.header(chapter)
  #st.write(chapter_questions[chapter]["question"])

  # Create radio buttons for the options
  radio_buttons = st.radio("Select an option:", chapter_questions[chapter]["options"])

  # If the option selected matches the correct answer, update the score
  if radio_buttons == chapter_questions[chapter]["answer"]:
    st.write("Correct!")
  else:
    st.write("Incorrect. The correct answer is " + chapter_questions[chapter]["answer"])

  # Show the word hint or the time hint
  if st.button("Word hint"):
    st.write(chapter_questions[chapter]["Word Hint"])
  elif st.button("Time hint"):
    st.write(chapter_questions[chapter]["Time Hint"])

# Display the final score
st.write(f"Final Score: {score}/{len(df)}")
