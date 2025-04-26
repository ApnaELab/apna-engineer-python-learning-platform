import streamlit as st
import json
import os
from pathlib import Path

# Setup page configuration
st.set_page_config(
    page_title="Python Learning Platform",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for progress tracking
if "completed_lessons" not in st.session_state:
    # Check if a progress file exists and load it
    progress_file = Path("user_progress.json")
    if progress_file.exists():
        with open(progress_file, "r") as f:
            st.session_state.completed_lessons = json.load(f)
    else:
        st.session_state.completed_lessons = {}

# Function to save progress
def save_progress():
    with open("user_progress.json", "w") as f:
        json.dump(st.session_state.completed_lessons, f)

# Main page content
st.title("🐍 Python Learning Platform for Beginners")

st.markdown("""
Welcome to your interactive Python learning journey! This platform is designed to help you learn Python 
from the absolute basics to intermediate concepts in a structured and interactive way.

## How to use this platform:
1. **Navigate** through the lessons using the sidebar
2. **Read** the explanations and examples
3. **Try** the interactive code examples 
4. **Complete** the exercises to test your knowledge
5. **Track** your progress as you go

## Learning Path:
- **Python Basics**: Introduction, Syntax, Variables, and Comments
- **Data Types**: Numbers, Strings, and Boolean
- **Control Flow**: Conditions, Loops, and Decision Making
- **Functions**: Creating and Using Functions
- **Data Structures**: Lists, Dictionaries, Tuples, and Sets
- **File Operations**: Reading and Writing Files
- **Error Handling**: Try/Except Statements
- **Data Visualization**: Charts, Graphs, and Visual Representations
- **Data Analysis**: Data Manipulation, Transformation, and Statistical Analysis

Let's get started by selecting a lesson from the sidebar!
""")

# Display progress
st.subheader("Your Learning Progress")

# Define all lessons
lessons = [
    "Python Basics", 
    "Data Types", 
    "Control Flow", 
    "Functions", 
    "Data Structures", 
    "File Operations", 
    "Error Handling",
    "Data Visualization",
    "Data Analysis"
]

# Create a progress bar
total_completed = sum(st.session_state.completed_lessons.get(lesson, 0) for lesson in lessons)
total_lessons = len(lessons)
progress_percentage = total_completed / total_lessons

st.progress(progress_percentage)
st.write(f"Overall progress: {int(progress_percentage * 100)}% completed")

# Display progress for each lesson
st.write("Lesson Status:")
for lesson in lessons:
    status = "✅ Completed" if st.session_state.completed_lessons.get(lesson, 0) == 1 else "⏳ In Progress"
    st.write(f"- {lesson}: {status}")

st.markdown("""
## Start Learning

Choose a lesson from the sidebar to begin your Python learning journey!

## About This Platform

This interactive platform is built with Streamlit and focuses on providing a hands-on 
learning experience for Python beginners. Each lesson includes explanations, examples, 
and interactive exercises to help you learn effectively.
""")
