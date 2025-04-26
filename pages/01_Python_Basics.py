import streamlit as st
from utils import lesson_ui, create_code_executor, create_exercise

def lesson_content():
    st.markdown("""
    # Python Basics
    
    Welcome to your first Python lesson! Let's start with the absolute basics.
    
    ## What is Python?
    
    Python is a high-level, interpreted programming language known for its readability and simplicity. 
    It's widely used in:
    - Web development
    - Data analysis
    - Artificial intelligence
    - Scientific computing
    - Automation
    
    ## Python Syntax
    
    Python is designed to be readable with a clean syntax that uses indentation 
    (whitespace) to define code blocks. This makes Python code look neat and consistent.
    
    ### Hello World
    
    Let's start with the classic "Hello, World!" program:
    """)
    
    code1 = """print("Hello, World!")"""
    st.code(code1, language="python")
    
    st.markdown("Try it yourself:")
    create_code_executor(code1)
    
    st.markdown("""
    ## Variables
    
    Variables are containers for storing data values. Python has no command for declaring a variable. 
    A variable is created the moment you first assign a value to it.
    """)
    
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
    
    st.markdown("Try creating your own variables:")
    create_code_executor(code2)
    
    st.markdown("""
    ## Comments
    
    Comments are notes in your code that are not executed. They help explain what your code does.
    
    - Single-line comments start with `#`
    - Multi-line comments are enclosed in triple quotes `'''` or `"""`
    """)
    
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
    st.markdown("Try adding your own comments:")
    create_code_executor(code3)
    
    st.markdown("""
    ## Basic Input and Output
    
    Python allows you to interact with users through input and output.
    - `print()` function displays output to the user
    - `input()` function captures input from the user
    """)
    
    code4 = """# Basic output
print("Welcome to Python!")

# Input and output
name = input("What is your name? ")
print("Hello,", name)
"""
    st.code(code4, language="python")
    st.markdown("""
    **Note:** In this interactive environment, the `input()` function won't work exactly 
    like it does in a typical Python environment. Let's try a modified example:
    """)
    
    code5 = """# Let's simulate input
name = "Alice"  # Normally this would be: name = input("What is your name? ")
print("Hello,", name)

# Try changing the name to your name
"""
    create_code_executor(code5)
    
    st.markdown("## Exercise: Your First Program")
    
    exercise_passed = create_exercise(
        "Create a program that defines two variables: your_name and your_age, then prints a message saying 'My name is [your_name] and I am [your_age] years old.'",
        """your_name = "Python Learner"
your_age = 25
print("My name is", your_name, "and I am", your_age, "years old.")"""
    )
    
    return exercise_passed

# Render the lesson using the utility function
lesson_ui("Python Basics", lesson_content)
