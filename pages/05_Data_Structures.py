import streamlit as st
from utils import lesson_ui, create_code_executor, create_exercise

def lesson_content():
    st.markdown("""
    # Data Structures
    
    Python has four built-in data structures: lists, tuples, dictionaries, and sets.
    Each has its own characteristics and use cases.
    
    ## Lists
    
    Lists are ordered, mutable collections that can contain items of different types:
    """)
    
    code1 = """# Creating lists
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "hello", 3.14, True]

# Accessing list elements
print(fruits[0])      # First element (index 0)
print(fruits[-1])     # Last element

# Changing elements
fruits[1] = "blueberry"
print(fruits)

# List methods
fruits.append("orange")     # Add to the end
print(fruits)

fruits.insert(1, "mango")   # Insert at index 1
print(fruits)

fruits.remove("cherry")     # Remove by value
print(fruits)

popped_fruit = fruits.pop() # Remove and return the last item
print(popped_fruit)
print(fruits)

# List operations
numbers = [1, 2, 3]
more_numbers = [4, 5, 6]

# Concatenation
combined = numbers + more_numbers
print(combined)

# Repetition
repeated = numbers * 3
print(repeated)

# Length
print(len(fruits))

# Checking if an item exists
print("apple" in fruits)
print("pear" in fruits)

# Slicing
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])   # Elements from index 1 to 3
print(numbers[:3])    # Elements from start to index 2
print(numbers[2:])    # Elements from index 2 to end
print(numbers[:])     # Copy of the entire list
"""
    st.code(code1, language="python")
    
    st.markdown("Try list operations:")
    create_code_executor(code1)
    
    st.markdown("""
    ### Common List Methods and Operations
    """)
    
    code2 = """# Sorting
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()             # Sort in-place
print(numbers)

fruits = ["orange", "apple", "cherry"]
print(sorted(fruits))      # Returns a new sorted list, original unchanged
print(fruits)              # Original list unchanged

# Reversing
numbers.reverse()          # Reverse in-place
print(numbers)
print(list(reversed(numbers)))  # Returns a new reversed list

# Finding index
fruits = ["apple", "banana", "cherry", "apple"]
print(fruits.index("cherry"))  # Index of first occurrence

# Counting occurrences
print(fruits.count("apple"))

# List comprehension - a concise way to create lists
squares = [x**2 for x in range(1, 6)]
print(squares)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)
"""
    st.code(code2, language="python")
    
    st.markdown("Try more list methods:")
    create_code_executor(code2)
    
    st.markdown("""
    ## Tuples
    
    Tuples are ordered, immutable collections. Once created, you cannot modify a tuple:
    """)
    
    code3 = """# Creating tuples
coordinates = (10, 20)
mixed_tuple = (1, "hello", 3.14)

# Tuple with one element (note the comma)
single_item = (42,)
print(type(single_item))

# Accessing tuple elements
print(coordinates[0])
print(coordinates[1])

# Attempting to modify a tuple will cause an error
# coordinates[0] = 15  # This would cause a TypeError

# Tuple unpacking
x, y = coordinates
print(f"X: {x}, Y: {y}")

# Tuple methods
numbers = (1, 2, 3, 2, 4, 2)
print(numbers.count(2))  # Count occurrences of 2
print(numbers.index(3))  # Index of first occurrence of 3

# Tuples are immutable but their elements can be mutable
mutable_inside = ([1, 2], [3, 4])
print(mutable_inside)
mutable_inside[0].append(5)  # Modify the list inside the tuple
print(mutable_inside)
"""
    st.code(code3, language="python")
    
    st.markdown("Try tuple operations:")
    create_code_executor(code3)
    
    st.markdown("""
    ## Dictionaries
    
    Dictionaries are unordered collections of key-value pairs:
    """)
    
    code4 = """# Creating dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing dictionary values
print(person["name"])

# Alternative way to access (safer)
print(person.get("age"))
print(person.get("job", "Not specified"))  # Provides default if key doesn't exist

# Modifying dictionaries
person["age"] = 31          # Changing a value
person["job"] = "Engineer"  # Adding a new key-value pair
print(person)

# Dictionary methods
keys = person.keys()      # View of all keys
values = person.values()  # View of all values
items = person.items()    # View of all key-value pairs

print("Keys:", list(keys))
print("Values:", list(values))
print("Items:", list(items))

# Removing items
removed_age = person.pop("age")  # Remove and return a value
print(f"Removed age: {removed_age}")
print(person)

# Checking if a key exists
print("name" in person)
print("gender" in person)

# Dictionary comprehension
squares = {x: x**2 for x in range(6)}
print(squares)
"""
    st.code(code4, language="python")
    
    st.markdown("Try dictionary operations:")
    create_code_executor(code4)
    
    st.markdown("""
    ## Sets
    
    Sets are unordered collections of unique elements:
    """)
    
    code5 = """# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

# Creating a set from a list (removes duplicates)
numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_with_duplicates)
print(unique_numbers)

# Adding elements
fruits.add("orange")
print(fruits)

# Removing elements
fruits.remove("banana")  # Raises error if not found
print(fruits)

fruits.discard("mango")  # No error if not found
print(fruits)

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union: elements in either set
print(set1 | set2)  # or set1.union(set2)

# Intersection: elements in both sets
print(set1 & set2)  # or set1.intersection(set2)

# Difference: elements in set1 but not in set2
print(set1 - set2)  # or set1.difference(set2)

# Symmetric difference: elements in either set but not in both
print(set1 ^ set2)  # or set1.symmetric_difference(set2)

# Checking if an element is in a set
print("apple" in fruits)
print("banana" in fruits)

# Checking if a set is a subset/superset of another
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print(set_a.issubset(set_b))
print(set_b.issuperset(set_a))
"""
    st.code(code5, language="python")
    
    st.markdown("Try set operations:")
    create_code_executor(code5)
    
    st.markdown("""
    ## Nested Data Structures
    
    Python data structures can be nested within each other:
    """)
    
    code6 = """# List of dictionaries
students = [
    {"name": "Alice", "grade": "A", "subjects": ["Math", "Science"]},
    {"name": "Bob", "grade": "B", "subjects": ["History", "English"]},
    {"name": "Charlie", "grade": "A", "subjects": ["Science", "Art"]}
]

# Accessing nested elements
print(students[0]["name"])
print(students[1]["subjects"][0])

# Dictionary with lists and other dictionaries
school = {
    "name": "Lincoln High",
    "classes": ["Math", "Science", "History", "English", "Art"],
    "teachers": {
        "Math": "Mr. Johnson",
        "Science": "Mrs. Smith",
        "History": "Ms. Lee"
    }
}

print(school["classes"][2])
print(school["teachers"]["Science"])

# Adding to nested structures
students[0]["subjects"].append("English")
print(students[0])

school["teachers"]["Art"] = "Mr. Davis"
print(school["teachers"])
"""
    st.code(code6, language="python")
    
    st.markdown("Try nested data structures:")
    create_code_executor(code6)
    
    st.markdown("""
    ## Exercises: Data Structures
    """)
    
    # First exercise
    exercise1_passed = create_exercise(
        "Create a list of dictionaries representing books with 'title', 'author', and 'year' keys. Add at least 3 books, then write code to print the title of the second book.",
        """books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
]

print(books[1]["title"])"""
    )
    
    # Second exercise (only shown if first one passes)
    if exercise1_passed:
        exercise2_passed = create_exercise(
            "Create a function that takes a list of numbers and returns a new list containing only the unique even numbers from the original list, sorted in ascending order.",
            """def get_unique_even_numbers(numbers):
    # Create a set of even numbers
    even_set = {num for num in numbers if num % 2 == 0}
    # Convert back to a list and sort
    return sorted(list(even_set))

numbers = [10, 5, 2, 7, 8, 2, 10, 12, 3]
result = get_unique_even_numbers(numbers)
print(result)"""
        )
    else:
        exercise2_passed = False
    
    return exercise1_passed and exercise2_passed

# Render the lesson using the utility function
lesson_ui("Data Structures", lesson_content)
