import streamlit as st
from utils import lesson_ui, create_code_executor, create_exercise

def lesson_content():
    st.markdown("""
    # Error Handling
    
    In Python, errors and exceptions happen when something goes wrong in your code.
    Error handling allows you to manage these situations gracefully.
    
    ## Types of Errors
    
    Python has many built-in exceptions:
    
    1. **SyntaxError**: When the parser detects an incorrect statement
    2. **TypeError**: When an operation is applied to an object of inappropriate type
    3. **NameError**: When a local or global name is not found
    4. **IndexError**: When a sequence index is out of range
    5. **KeyError**: When a dictionary key is not found
    6. **ValueError**: When a function gets an argument of correct type but improper value
    7. **FileNotFoundError**: When a file or directory is requested but doesn't exist
    8. **ZeroDivisionError**: When division or modulo by zero is performed
    
    Let's see some examples:
    """)
    
    code1 = """# SyntaxError
# print("Hello world"  # Missing closing parenthesis - uncomment to see error

# TypeError
print("Hello" + 5)  # Can't add string and integer

# NameError
# print(undefined_variable)  # Variable not defined - uncomment to see error

# IndexError
my_list = [1, 2, 3]
print(my_list[10])  # Index out of range

# KeyError
my_dict = {"name": "Alice", "age": 30}
print(my_dict["address"])  # Key doesn't exist

# ValueError
int("not a number")  # Can't convert string to integer

# ZeroDivisionError
print(10 / 0)  # Division by zero
"""
    st.code(code1, language="python")
    
    st.markdown("""
    **Note**: The code above will produce errors. That's intentional! Let's learn how to handle them.
    
    ## Try-Except Blocks
    
    The `try-except` block is used to catch and handle exceptions:
    """)
    
    code2 = """# Basic try-except
try:
    # This will cause a ZeroDivisionError
    result = 10 / 0
    print(result)
except:
    print("An error occurred!")

# Catching specific exceptions
try:
    # This will cause a ZeroDivisionError
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero!")

# Multiple except blocks
try:
    # Choose one of these to test different exceptions
    # num = int("not a number")  # ValueError
    num = 10 / 0                # ZeroDivisionError
    # print(undefined_variable)   # NameError
except ValueError:
    print("Error: Invalid value!")
except ZeroDivisionError:
    print("Error: Division by zero!")
except:
    print("Some other error occurred!")

# Accessing the exception information
try:
    num = int("not a number")
except ValueError as e:
    print(f"Error message: {e}")
    print(f"Error type: {type(e).__name__}")
"""
    st.code(code2, language="python")
    
    st.markdown("Try error handling:")
    create_code_executor(code2)
    
    st.markdown("""
    ## Try-Except-Else-Finally
    
    Python's `try` statement has two optional clauses:
    
    - `else`: Executed if no exception occurs
    - `finally`: Executed always, regardless of whether an exception occurred
    """)
    
    code3 = """# Try-except-else
try:
    num = int("10")
except ValueError:
    print("Invalid number!")
else:
    print(f"Conversion successful! Number is {num}")

# Try-except-finally
try:
    num = int("10")
    print(f"Number is {num}")
except ValueError:
    print("Invalid number!")
finally:
    print("This always executes!")

# Complete example combining all
try:
    num = int(input("Enter a number: "))  # For our example, let's simulate input
    # num = int("10")  # Uncomment to try successful conversion
    # num = int("abc")  # Uncomment to try failed conversion
    result = 100 / num
except ValueError:
    print("Error: That's not a valid number!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print(f"100 divided by {num} is {result}")
finally:
    print("Execution completed!")
"""
    st.code(code3, language="python")
    
    st.markdown("Try complete error handling:")
    create_code_executor(code3)
    
    st.markdown("""
    ## Raising Exceptions
    
    You can raise exceptions using the `raise` statement:
    """)
    
    code4 = """# Raising a simple exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 18:
        raise ValueError("Must be at least 18 years old")
    return "Age is valid"

# Try calling with different ages
try:
    result = check_age(20)  # Should work
    # result = check_age(15)  # Should raise "Must be at least 18"
    # result = check_age(-5)  # Should raise "Age cannot be negative"
    print(result)
except ValueError as e:
    print(f"Validation error: {e}")

# Raising with custom message
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

try:
    result = divide(10, 2)  # Should work
    # result = divide(10, 0)  # Should raise the custom error
    print(f"Result: {result}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
"""
    st.code(code4, language="python")
    
    st.markdown("Try raising exceptions:")
    create_code_executor(code4)
    
    st.markdown("""
    ## Creating Custom Exceptions
    
    You can define your own exception classes by inheriting from the built-in `Exception` class:
    """)
    
    code5 = """# Define a custom exception
class InsufficientFundsError(Exception):
    # Raised when a withdrawal would result in a negative balance
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.deficit = amount - balance
        super().__init__(f"Insufficient funds: balance=${balance}, requested=${amount}, deficit=${self.deficit}")

# Use the custom exception
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance
        
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

# Test the custom exception
account = BankAccount(100)
try:
    # Try different operations
    account.deposit(50)
    print(f"Balance after deposit: ${account.balance}")
    
    account.withdraw(75)
    print(f"Balance after withdrawal: ${account.balance}")
    
    account.withdraw(100)  # This should raise InsufficientFundsError
    print("This line won't execute if an exception is raised")
except ValueError as e:
    print(f"Value Error: {e}")
except InsufficientFundsError as e:
    print(f"Custom Error: {e}")
    print(f"You need ${e.deficit} more to complete this withdrawal")
"""
    st.code(code5, language="python")
    
    st.markdown("Try custom exceptions:")
    create_code_executor(code5)
    
    st.markdown("""
    ## Best Practices for Error Handling
    
    1. **Be specific**: Catch specific exceptions rather than using a blanket `except`.
    2. **Keep try blocks small**: Include only code that might raise an exception.
    3. **Use else clause**: For code that should run only if no exceptions occurred.
    4. **Always clean up**: Use `finally` for cleanup code.
    5. **Log errors**: In real applications, log exceptions for debugging.
    6. **Provide useful error messages**: Make error messages clear and informative.
    
    Here's an example incorporating these practices:
    """)
    
    code6 = """def process_file(filename):
    file = None
    try:
        # Only the potentially problematic code in try block
        file = open(filename, 'r')
    except FileNotFoundError:
        # Specific exception
        print(f"Error: The file '{filename}' was not found.")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'.")
        return None
    except Exception as e:
        # Catch other exceptions as a last resort
        print(f"Unexpected error: {e}")
        return None
    else:
        # Only runs if no exception
        content = file.read()
        print(f"Successfully read {len(content)} characters from file.")
        return content
    finally:
        # Always cleanup
        if file:
            file.close()
            print("File closed.")

# Since we can't access actual files in this environment, 
# let's simulate the function with different exceptions
import io

def simulate_process_file(scenario):
    if scenario == "normal":
        # Simulate normal operation
        print("Simulating normal file processing:")
        file = io.StringIO("This is file content")
        content = file.read()
        print(f"Successfully read {len(content)} characters from file.")
        file.close()
        print("File closed.")
        return content
    elif scenario == "not_found":
        # Simulate FileNotFoundError
        print("Simulating file not found:")
        try:
            raise FileNotFoundError("File not found")
        except FileNotFoundError:
            print("Error: The file 'nonexistent.txt' was not found.")
            return None
    elif scenario == "permission":
        # Simulate PermissionError
        print("Simulating permission error:")
        try:
            raise PermissionError("Permission denied")
        except PermissionError:
            print("Error: No permission to read 'protected.txt'.")
            return None
    else:
        # Simulate unexpected error
        print("Simulating unexpected error:")
        try:
            raise RuntimeError("Something went wrong")
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

# Test the scenarios
print(simulate_process_file("normal"))
print()
print(simulate_process_file("not_found"))
print()
print(simulate_process_file("permission"))
print()
print(simulate_process_file("unexpected"))
"""
    st.code(code6, language="python")
    
    st.markdown("Try best practices:")
    create_code_executor(code6)
    
    st.markdown("""
    ## Exercises: Error Handling
    """)
    
    # First exercise
    exercise1_passed = create_exercise(
        "Write a function called 'safe_division' that takes two parameters and returns their division. Handle potential ZeroDivisionError and TypeError exceptions with appropriate error messages.",
        """def safe_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both inputs must be numbers."

# Test cases
print(safe_division(10, 2))  # Should return 5.0
print(safe_division(10, 0))  # Should handle zero division
print(safe_division("10", 2))  # Should handle type error"""
    )
    
    # Second exercise (only shown if first one passes)
    if exercise1_passed:
        exercise2_passed = create_exercise(
            "Create a function called 'get_dict_value' that accepts a dictionary, a key, and a default value. If the key exists in the dictionary, return its value. If the key doesn't exist, return the default value. Use a try-except block to handle potential KeyError.",
            """def get_dict_value(dictionary, key, default=None):
    try:
        return dictionary[key]
    except KeyError:
        return default

# Test cases
person = {"name": "Alice", "age": 30}
print(get_dict_value(person, "name"))  # Should return "Alice"
print(get_dict_value(person, "address"))  # Should return None
print(get_dict_value(person, "address", "Unknown"))  # Should return "Unknown"""
        )
    else:
        exercise2_passed = False
    
    return exercise1_passed and exercise2_passed

# Render the lesson using the utility function
lesson_ui("Error Handling", lesson_content)
