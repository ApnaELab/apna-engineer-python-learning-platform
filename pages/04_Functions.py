import streamlit as st
from utils import lesson_ui, create_code_executor, create_exercise

def lesson_content():
    st.markdown("""
    # Functions
    
    Functions are blocks of reusable code designed to perform a specific task.
    They help in organizing code, making it more modular and easier to understand.
    
    ## Defining Functions
    
    In Python, functions are defined using the `def` keyword:
    """)
    
    code1 = """# Basic function definition
def greet():
    print("Hello, world!")

# Function call
greet()
"""
    st.code(code1, language="python")
    
    st.markdown("Try defining and calling a function:")
    create_code_executor(code1)
    
    st.markdown("""
    ## Functions with Parameters
    
    Functions can accept input values called parameters:
    """)
    
    code2 = """# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

# Call with different arguments
greet_person("Alice")
greet_person("Bob")

# Function with multiple parameters
def describe_pet(name, animal_type="dog"):
    print(f"I have a {animal_type} named {name}.")

# Call with different parameters
describe_pet("Buddy")
describe_pet("Whiskers", "cat")
"""
    st.code(code2, language="python")
    
    st.markdown("Try functions with parameters:")
    create_code_executor(code2)
    
    st.markdown("""
    ## Return Values
    
    Functions can return values using the `return` statement:
    """)
    
    code3 = """# Function that returns a value
def square(number):
    return number * number

# Call and use the returned value
result = square(5)
print(f"The square of 5 is {result}")

# Function with multiple returns
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

name = get_formatted_name("john", "doe")
print(name)

# Function with conditional returns
def absolute_value(number):
    if number >= 0:
        return number
    else:
        return -number

print(f"Absolute value of 5: {absolute_value(5)}")
print(f"Absolute value of -5: {absolute_value(-5)}")
"""
    st.code(code3, language="python")
    
    st.markdown("Try functions with return values:")
    create_code_executor(code3)
    
    st.markdown("""
    ## Function Arguments
    
    Python provides different ways to pass arguments to functions:
    """)
    
    code4 = """# Positional arguments
def describe_city(city, country):
    print(f"{city} is in {country}")

describe_city("Paris", "France")

# Keyword arguments
describe_city(country="Japan", city="Tokyo")

# Default parameter values
def make_pizza(topping="cheese"):
    print(f"Making a {topping} pizza")

make_pizza()  # Uses the default
make_pizza("pepperoni")  # Overrides the default

# Variable number of arguments (*args)
def print_numbers(*numbers):
    print("Numbers:", numbers)  # numbers is a tuple

print_numbers(1, 2, 3, 4, 5)

# Variable number of keyword arguments (**kwargs)
def build_profile(**user_info):
    print("User Profile:")
    for key, value in user_info.items():
        print(f"{key}: {value}")

build_profile(name="Alice", age=30, occupation="Developer")
"""
    st.code(code4, language="python")
    
    st.markdown("Try different function argument types:")
    create_code_executor(code4)
    
    st.markdown("""
    ## Scope of Variables
    
    Variables defined inside a function have local scope, while variables defined 
    outside functions have global scope:
    """)
    
    code5 = """# Global variable
message = "Hello, Global!"

def show_message():
    # Local variable
    local_message = "Hello, Local!"
    print(local_message)  # Can access local variable
    print(message)  # Can access global variable

show_message()
print(message)  # Can access global variable
# print(local_message)  # This would cause an error - local_message is not defined globally

# Modifying global variables
def update_global():
    global message  # Declare that we want to use the global variable
    message = "Updated global message"

print("Before:", message)
update_global()
print("After:", message)
"""
    st.code(code5, language="python")
    
    st.markdown("Try variable scoping:")
    create_code_executor(code5)
    
    st.markdown("""
    ## Lambda Functions
    
    Lambda functions are small anonymous functions defined with the `lambda` keyword:
    """)
    
    code6 = """# Lambda function
double = lambda x: x * 2
print(double(5))

# Lambda with multiple parameters
sum_func = lambda x, y: x + y
print(sum_func(3, 4))

# Lambda with conditionals
is_even = lambda x: True if x % 2 == 0 else False
print(is_even(4))  # True
print(is_even(5))  # False

# Lambda with sorting
points = [(1, 2), (3, 1), (5, 4)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)  # Sorts by the second value in each tuple
"""
    st.code(code6, language="python")
    
    st.markdown("Try lambda functions:")
    create_code_executor(code6)
    
    st.markdown("""
    ## Exercises: Functions
    """)
    
    # First exercise
    exercise1_passed = create_exercise(
        "Write a function called 'calculate_area' that takes the radius of a circle as a parameter and returns the area of the circle (area = π * radius^2). Use 3.14 for π. Then call your function to find the area of a circle with radius 5.",
        """def calculate_area(radius):
    return 3.14 * radius ** 2

area = calculate_area(5)
print(area)"""
    )
    
    # Second exercise (only shown if first one passes)
    if exercise1_passed:
        exercise2_passed = create_exercise(
            "Write a function called 'is_palindrome' that takes a string as input and returns True if the string is a palindrome (reads the same forward and backward), and False otherwise. Test your function with the word 'radar'.",
            """def is_palindrome(text):
    # Remove spaces and convert to lowercase for more accurate comparison
    text = text.replace(" ", "").lower()
    return text == text[::-1]

result = is_palindrome("radar")
print(result)"""
        )
    else:
        exercise2_passed = False
    
    return exercise1_passed and exercise2_passed

# Render the lesson using the utility function
lesson_ui("Functions", lesson_content)
