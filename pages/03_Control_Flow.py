import streamlit as st
from utils import lesson_ui, create_code_executor, create_exercise

def lesson_content():
    st.markdown("""
    # Control Flow
    
    Control flow statements determine the order in which code is executed based on 
    certain conditions. Python provides several structures for control flow:
    
    ## Conditional Statements (if-elif-else)
    
    Conditional statements let your program make decisions:
    """)
    
    code1 = """# Basic if statement
age = 18

if age >= 18:
    print("You are an adult.")
    
# if-else statement
temperature = 15

if temperature > 25:
    print("It's a warm day.")
else:
    print("It's not so warm.")
    
# if-elif-else statement (multiple conditions)
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
"""
    st.code(code1, language="python")
    
    st.markdown("Try conditional statements:")
    create_code_executor(code1)
    
    st.markdown("""
    ### Nested Conditions
    
    You can nest conditional statements inside other conditional statements:
    """)
    
    code2 = """# Nested conditions
age = 20
has_license = True

if age >= 18:
    print("Age requirement met.")
    if has_license:
        print("You can drive.")
    else:
        print("You need a license to drive.")
else:
    print("You must be at least 18 to drive.")
"""
    st.code(code2, language="python")
    
    st.markdown("Try nested conditions:")
    create_code_executor(code2)
    
    st.markdown("""
    ## Loops
    
    Loops allow you to execute a block of code multiple times.
    
    ### For Loops
    
    For loops iterate over a sequence (like a list, tuple, string, etc.):
    """)
    
    code3 = """# Basic for loop with a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}s")
    
# For loop with range()
print("\nCounting from 0 to 4:")
for i in range(5):  # range(5) generates 0, 1, 2, 3, 4
    print(i)
    
# For loop with range(start, stop)
print("\nCounting from 1 to 5:")
for i in range(1, 6):  # range(1, 6) generates 1, 2, 3, 4, 5
    print(i)
    
# For loop with range(start, stop, step)
print("\nEven numbers from 0 to 10:")
for i in range(0, 11, 2):  # Step of 2
    print(i)
    
# For loop with a string
message = "Python"
print("\nLetters in Python:")
for char in message:
    print(char)
"""
    st.code(code3, language="python")
    
    st.markdown("Try for loops:")
    create_code_executor(code3)
    
    st.markdown("""
    ### While Loops
    
    While loops continue executing as long as a condition is True:
    """)
    
    code4 = """# Basic while loop
count = 0

while count < 5:
    print(f"Count is {count}")
    count += 1  # Increment count by 1
    
print("Loop finished")

# While loop with a flag variable
print("\nWhile loop with a condition:")
running = True
counter = 0

while running:
    print(f"Running... {counter}")
    counter += 1
    
    if counter >= 3:
        running = False  # Exit the loop
        
print("Stopped running")
"""
    st.code(code4, language="python")
    
    st.markdown("Try while loops:")
    create_code_executor(code4)
    
    st.markdown("""
    ## Loop Control Statements
    
    Python provides statements to control loop execution:
    """)
    
    code5 = """# break - exits the loop completely
print("Using break:")
for i in range(10):
    if i == 5:
        print("Breaking the loop")
        break
    print(i)
    
# continue - skips the current iteration and continues with the next
print("\nUsing continue:")
for i in range(10):
    if i % 2 == 0:  # If i is even
        continue
    print(i)  # Only print odd numbers
    
# Else clause in loops
# The else clause executes when the loop completes normally (not by break)
print("\nLoop with else:")
for i in range(3):
    print(i)
else:
    print("Loop completed successfully")
    
print("\nLoop with break and else:")
for i in range(3):
    print(i)
    if i == 1:
        break
else:
    print("This won't print because the loop was broken")
"""
    st.code(code5, language="python")
    
    st.markdown("Try loop control statements:")
    create_code_executor(code5)
    
    st.markdown("""
    ## Exercises: Control Flow
    """)
    
    # First exercise
    exercise1_passed = create_exercise(
        "Write a program that checks if a number is positive, negative, or zero. Use an if-elif-else structure.",
        """number = 10
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")"""
    )
    
    # Second exercise (only shown if first one passes)
    if exercise1_passed:
        exercise2_passed = create_exercise(
            "Write a program that uses a for loop to print all numbers from 1 to 10, but only print the even numbers. Use the continue statement to skip odd numbers.",
            """for i in range(1, 11):
    if i % 2 != 0:  # If i is odd
        continue
    print(i)"""
        )
    else:
        exercise2_passed = False
    
    return exercise1_passed and exercise2_passed

# Render the lesson using the utility function
lesson_ui("Control Flow", lesson_content)
