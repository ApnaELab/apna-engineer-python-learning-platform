import streamlit as st
from utils import lesson_ui, create_code_executor, create_exercise

def lesson_content():
    st.header("Data Types")
    
    st.write("Python has several built-in data types. In this lesson, we'll explore the fundamental ones:")
    
    st.subheader("Numbers")
    
    st.write("""Python supports two types of numbers:
    
    1. **Integers (int)**: Whole numbers without a decimal point
    2. **Floating-point numbers (float)**: Numbers with a decimal point
    
    Let's see some examples:
    """)
    
    code1 = """# Integers
age = 25
count = -10

# Floating-point numbers
height = 5.7
temperature = -2.5

# Print and check the types
print("Age:", age, "Type:", type(age))
print("Height:", height, "Type:", type(height))

# Basic operations
sum_result = age + count
product = height * 2
print("Sum:", sum_result)
print("Product:", product)
"""
    st.code(code1, language="python")
    
    st.write("Try it yourself:")
    create_code_executor(code1)
    
    st.subheader("Strings")
    
    st.write("""Strings are sequences of characters enclosed in quotes. Python allows single (`'`), 
    double (`"`), or triple quotes (`'''` or `"""`) for strings.""")
    
    code2 = """# Creating strings
name = "Alice"
message = 'Hello, Python!'
paragraph = '''This is a multi-line
string in Python.
It can span multiple lines.'''

# Print strings
print(name)
print(message)
print(paragraph)

# String operations
# 1. Concatenation (joining strings)
full_message = message + " My name is " + name
print(full_message)

# 2. Repetition
print("=" * 20)  # Print = character 20 times

# 3. Indexing (accessing individual characters)
first_char = name[0]  # Indexing starts from 0
print("First character:", first_char)

# 4. Slicing (getting a substring)
substring = name[1:3]  # Characters from index 1 to 2 (3 is exclusive)
print("Substring:", substring)

# 5. String length
print("Length of name:", len(name))
"""
    st.code(code2, language="python")
    
    st.write("Try string operations:")
    create_code_executor(code2)
    
    st.write("### String Methods")
    
    st.write("Python provides many useful methods for working with strings:")
    
    code3 = """text = "Python Programming"

# Convert to uppercase/lowercase
print(text.upper())
print(text.lower())

# Check if string starts/ends with specific text
print(text.startswith("Py"))
print(text.endswith("ing"))

# Find a substring
print(text.find("gram"))  # Returns the index of the substring

# Replace text
print(text.replace("Programming", "Coding"))

# Split string into a list
words = text.split()
print(words)

# Join list elements into a string
new_text = "-".join(words)
print(new_text)
"""
    st.code(code3, language="python")
    
    st.write("Try string methods:")
    create_code_executor(code3)
    
    st.subheader("Boolean")
    
    st.write("Boolean values represent truth values with two constants: `True` and `False`. They're often used in conditional statements and logical operations.")
    
    code4 = """# Boolean values
is_active = True
is_complete = False

print("Is active:", is_active)
print("Is complete:", is_complete)

# Comparison operators produce boolean results
x = 10
y = 5

print("x > y:", x > y)
print("x < y:", x < y)
print("x == y:", x == y)
print("x != y:", x != y)

# Logical operators with booleans
print("AND:", is_active and is_complete)  # True if both are True
print("OR:", is_active or is_complete)    # True if at least one is True
print("NOT:", not is_active)              # Inverts the boolean value

# Boolean in conditions
if is_active:
    print("The program is active")
else:
    print("The program is not active")
"""
    st.code(code4, language="python")
    
    st.write("Try boolean operations:")
    create_code_executor(code4)
    
    st.subheader("Type Conversion")
    
    st.write("Python allows you to convert between different data types:")
    
    code5 = """# Convert string to integer
age_str = "25"
age_int = int(age_str)
print("String to Integer:", age_int, type(age_int))

# Convert integer to string
count = 100
count_str = str(count)
print("Integer to String:", count_str, type(count_str))

# Convert string to float
price_str = "19.99"
price_float = float(price_str)
print("String to Float:", price_float, type(price_float))

# Convert float to integer (truncates decimal part)
height = 5.7
height_int = int(height)
print("Float to Integer:", height_int, type(height_int))

# Convert to boolean
print("Bool of 1:", bool(1))        # Any non-zero number is True
print("Bool of 0:", bool(0))        # 0 is False
print("Bool of empty string:", bool(""))  # Empty string is False
print("Bool of non-empty:", bool("hello"))  # Non-empty string is True
"""
    st.code(code5, language="python")
    
    st.write("Try type conversion:")
    create_code_executor(code5)
    
    st.subheader("Exercises: Data Types")
    
    # First exercise
    exercise1_solution = """celsius = 25.0
fahrenheit = celsius * 9/5 + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")"""

    exercise1_passed = create_exercise(
        "Create a program that takes a temperature in Celsius (as a float) and converts it to Fahrenheit using the formula: F = C * 9/5 + 32. Store the result in a variable called 'fahrenheit' and print it with a message.",
        exercise1_solution
    )
    
    # Second exercise
    if exercise1_passed:
        exercise2_solution = """text = "example"
uppercase_text = text.upper()
contains_a = 'A' in uppercase_text
print(contains_a)"""

        exercise2_passed = create_exercise(
            "Create a program that takes a string, converts it to uppercase, and checks if it contains the letter 'A'. Print the result as a boolean value.",
            exercise2_solution
        )
    else:
        exercise2_passed = False
    
    return exercise1_passed and exercise2_passed

# Render the lesson using the utility function
lesson_ui("Data Types", lesson_content)
