import streamlit as st
from utils import lesson_ui, create_code_executor, create_exercise

def lesson_content():
    st.header("Python Basics")
    
    st.write("Welcome to your first Python lesson! Let's start with the absolute basics.")
    
    st.subheader("What is Python?")
    
    st.write("""Python is a high-level, interpreted programming language known for its readability and simplicity. 
    It's widely used in:
    - Web development
    - Data analysis
    - Artificial intelligence
    - Scientific computing
    - Automation""")
    
    st.subheader("Python Syntax")
    
    st.write("""Python is designed to be readable with a clean syntax that uses indentation 
    (whitespace) to define code blocks. This makes Python code look neat and consistent.""")
    
    st.subheader("Hello World")
    
    st.write("Let's start with the classic \"Hello, World!\" program:")
    
    code1 = """print("Hello, World!")"""
    st.code(code1, language="python")
    
    st.write("Try it yourself:")
    create_code_executor(code1)
    
    st.subheader("Variables")
    
    st.write("""Variables are containers for storing data values. Python has no command for declaring a variable. 
    A variable is created the moment you first assign a value to it.""")
    
    code2 = """# Creating variables
name = "Alice"
age = 25
height = 5.7

# Using variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
"""
    st.code(code2, language="python")
    
    st.write("Try creating your own variables:")
    create_code_executor(code2)
    
    st.subheader("Comments")
    
    st.write("""Comments are notes in your code that are not executed. They help explain what your code does.""")
    
    st.write("- Single-line comments start with `#`")
    st.write("- Multi-line comments are enclosed in triple quotes `'''` or `\"\"\"`")
    
    code3 = """# This is a single-line comment

'''
This is a
multi-line comment
'''

# Code with comments
name = "Bob"  # Assign the name Bob to the variable
print(name)   # Print the name
"""
    st.code(code3, language="python")
    st.write("Try adding your own comments:")
    create_code_executor(code3)
    
    st.subheader("Basic Input and Output")
    
    st.write("""Python allows you to interact with users through input and output.
    - `print()` function displays output to the user
    - `input()` function captures input from the user""")
    
    code4 = """# Basic output
print("Welcome to Python!")

# Input and output
name = input("What is your name? ")
print("Hello,", name)
"""
    st.code(code4, language="python")
    
    st.write("Note: In this interactive environment, the input() function won't work exactly like it does in a typical Python environment. Let's try a modified example:")
    
    code5 = """# Let's simulate input
name = "Alice"  # Normally this would be: name = input("What is your name? ")
print("Hello,", name)

# Try changing the name to your name
"""
    create_code_executor(code5)
    
    st.subheader("Exercise: Your First Program")
    
    # Define the solution separately 
    solution = '''your_name = "Python Learner"
your_age = 25
print("My name is", your_name, "and I am", your_age, "years old.")'''
    
    # Pass the solution to the exercise function
    exercise_passed = create_exercise(
        "Create a program that defines two variables: your_name and your_age, then prints a message saying 'My name is [your_name] and I am [your_age] years old.'",
        solution
    )
    
    return exercise_passed

# Render the lesson using the utility function
lesson_ui("Python Basics", lesson_content)
