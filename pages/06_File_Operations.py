import streamlit as st
from utils import lesson_ui, create_code_executor, create_exercise

def lesson_content():
    st.markdown("""
    # File Operations
    
    Python allows you to work with files to read and write data. This is essential for 
    persisting information between program runs and processing external data.
    
    ## Opening and Closing Files
    
    The basic syntax for file operations is:
    """)
    
    code1 = """# Opening a file in read mode
file = open('example.txt', 'r')
# Operations on the file
file.close()  # Always close the file when done

# Better approach: 'with' statement automatically closes the file
with open('example.txt', 'r') as file:
    # Operations on the file
    pass  # The file is automatically closed when the block ends
"""
    st.code(code1, language="python")
    
    st.markdown("""
    **Note about this interactive environment**: In this environment, we don't have 
    access to the file system directly. Instead, we'll simulate file operations by 
    creating example files in memory.
    
    ## File Modes
    
    Python supports various file modes:
    
    - `'r'`: Read (default)
    - `'w'`: Write (creates a new file or truncates an existing one)
    - `'a'`: Append (adds to the end of the file)
    - `'r+'`: Read and write
    - `'b'`: Binary mode (e.g., `'rb'` for reading binary files)
    
    ## Reading from Files
    
    There are multiple ways to read data from files:
    """)
    
    code2 = """# Let's simulate a file in memory for our examples
from io import StringIO

# Create a simulated file with some content
file_content = '''This is line 1.
This is line 2.
This is line 3.
This is line 4.
This is line 5.'''

# Create a file-like object
file = StringIO(file_content)

# Reading the entire file at once
file.seek(0)  # Go to the beginning of the file
content = file.read()
print("Entire file:")
print(content)

# Reading line by line
file.seek(0)
print("\nLine by line:")
for line in file:
    print(line.strip())  # strip() removes the trailing newline

# Reading all lines into a list
file.seek(0)
lines = file.readlines()
print("\nAll lines as a list:")
print(lines)

# Reading a specific number of characters
file.seek(0)
first_10_chars = file.read(10)
print("\nFirst 10 characters:")
print(first_10_chars)
"""
    st.code(code2, language="python")
    
    st.markdown("Try reading from a simulated file:")
    create_code_executor(code2)
    
    st.markdown("""
    ## Writing to Files
    
    You can write data to files using the `write()` and `writelines()` methods:
    """)
    
    code3 = """# Create a file-like object for writing
output_file = StringIO()

# Writing a string to a file
output_file.write("Hello, World!\\n")
output_file.write("This is a new line.")

# Check what was written
print("Contents of the file after writing:")
print(output_file.getvalue())

# Create a new file-like object
output_file2 = StringIO()

# Writing multiple lines at once
lines_to_write = [
    "Line 1\\n",
    "Line 2\\n",
    "Line 3\\n"
]
output_file2.writelines(lines_to_write)

# Check what was written
print("\\nContents of the second file:")
print(output_file2.getvalue())
"""
    st.code(code3, language="python")
    
    st.markdown("Try writing to a simulated file:")
    create_code_executor(code3)
    
    st.markdown("""
    ## Appending to Files
    
    You can add data to the end of a file using append mode:
    """)
    
    code4 = """# Create a file with some initial content
append_file = StringIO("Initial content.\\n")

# Simulate appending to the file
current_content = append_file.getvalue()
append_file = StringIO()
append_file.write(current_content)
append_file.write("Appended line 1.\\n")
append_file.write("Appended line 2.\\n")

# Check the result
print("File after appending:")
print(append_file.getvalue())
"""
    st.code(code4, language="python")
    
    st.markdown("Try appending to a simulated file:")
    create_code_executor(code4)
    
    st.markdown("""
    ## Working with File Paths
    
    Python's `os` and `pathlib` modules provide tools for working with file paths:
    """)
    
    code5 = """import os
from pathlib import Path

# Current working directory
print("Current working directory:", os.getcwd())

# Joining paths
file_path = os.path.join("folder", "subfolder", "file.txt")
print("Joined path:", file_path)

# Path components
print("Directory name:", os.path.dirname(file_path))
print("File name:", os.path.basename(file_path))

# Using pathlib (more modern and object-oriented)
path = Path("folder") / "subfolder" / "file.txt"
print("Pathlib path:", path)
print("Parent directory:", path.parent)
print("File name:", path.name)
print("File stem:", path.stem)
print("File suffix:", path.suffix)
"""
    st.code(code5, language="python")
    
    st.markdown("Try file path operations:")
    create_code_executor(code5)
    
    st.markdown("""
    ## Working with Different File Types
    
    ### CSV Files
    
    CSV (Comma-Separated Values) files are common for tabular data:
    """)
    
    code6 = """import csv
from io import StringIO

# Sample CSV data
csv_data = '''name,age,city
Alice,28,New York
Bob,32,San Francisco
Charlie,45,Chicago
'''

# Create a file-like object
csv_file = StringIO(csv_data)

# Reading CSV
print("Reading CSV data:")
reader = csv.reader(csv_file)
header = next(reader)  # Get the header row
print(f"Header: {header}")

for row in reader:
    print(f"Name: {row[0]}, Age: {row[1]}, City: {row[2]}")

# Writing CSV data
output_csv = StringIO()
writer = csv.writer(output_csv)

# Write header and rows
writer.writerow(['name', 'age', 'city'])
writer.writerow(['David', '35', 'Boston'])
writer.writerow(['Eva', '29', 'Seattle'])

print("\\nWritten CSV data:")
print(output_csv.getvalue())

# Using DictReader and DictWriter (maps to/from dictionaries)
csv_file.seek(0)  # Reset to beginning
dict_reader = csv.DictReader(csv_file)

print("\\nReading with DictReader:")
for row in dict_reader:
    print(f"Name: {row['name']}, Age: {row['age']}, City: {row['city']}")

# DictWriter
output_dict_csv = StringIO()
fieldnames = ['name', 'age', 'city']
dict_writer = csv.DictWriter(output_dict_csv, fieldnames=fieldnames)

dict_writer.writeheader()
dict_writer.writerow({'name': 'Frank', 'age': '41', 'city': 'Dallas'})
dict_writer.writerow({'name': 'Grace', 'age': '38', 'city': 'Miami'})

print("\\nWritten with DictWriter:")
print(output_dict_csv.getvalue())
"""
    st.code(code6, language="python")
    
    st.markdown("Try CSV file operations:")
    create_code_executor(code6)
    
    st.markdown("""
    ### JSON Files
    
    JSON (JavaScript Object Notation) is widely used for structured data:
    """)
    
    code7 = """import json
from io import StringIO

# Python data structure
data = {
    "people": [
        {"name": "Alice", "age": 28, "city": "New York"},
        {"name": "Bob", "age": 32, "city": "San Francisco"},
        {"name": "Charlie", "age": 45, "city": "Chicago"}
    ],
    "company": "Example Corp",
    "founded": 2010
}

# Convert Python object to JSON string
json_string = json.dumps(data, indent=4)
print("JSON string:")
print(json_string)

# Parse JSON string back to Python
parsed_data = json.loads(json_string)
print("\\nParsed back to Python:")
print(f"Company: {parsed_data['company']}")
print(f"First person: {parsed_data['people'][0]['name']}")

# Writing JSON to a file
json_file = StringIO()
json.dump(data, json_file, indent=4)
print("\\nJSON file content:")
print(json_file.getvalue())

# Reading JSON from a file
json_input = StringIO('''{
    "employees": [
        {"name": "David", "position": "Manager"},
        {"name": "Eva", "position": "Developer"}
    ],
    "location": "New York"
}''')

file_data = json.load(json_input)
print("\\nLoaded from file:")
print(f"Location: {file_data['location']}")
print(f"Employees: {len(file_data['employees'])}")
"""
    st.code(code7, language="python")
    
    st.markdown("Try JSON file operations:")
    create_code_executor(code7)
    
    st.markdown("""
    ## Exercises: File Operations
    """)
    
    # First exercise
    exercise1_passed = create_exercise(
        "Create a function that reads a CSV string (simulating a file) containing names and scores, and returns a list of dictionaries with those values. Then call the function with sample data.",
        """def read_csv_scores(csv_string):
    import csv
    from io import StringIO
    
    result = []
    csv_file = StringIO(csv_string)
    reader = csv.DictReader(csv_file)
    
    for row in reader:
        result.append(row)
    
    return result

# Test with sample data
csv_data = '''name,score
Alice,85
Bob,92
Charlie,78
'''

scores = read_csv_scores(csv_data)
print(scores)"""
    )
    
    # Second exercise (only shown if first one passes)
    if exercise1_passed:
        exercise2_passed = create_exercise(
            "Create a function that takes a list of dictionaries (each with 'name' and 'age' keys) and converts it to a JSON string with an indentation of 2 spaces. Test it with sample data.",
            """def convert_to_json(data):
    import json
    return json.dumps(data, indent=2)

# Test with sample data
people = [
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 32},
    {"name": "Charlie", "age": 45}
]

json_string = convert_to_json(people)
print(json_string)"""
        )
    else:
        exercise2_passed = False
    
    return exercise1_passed and exercise2_passed

# Render the lesson using the utility function
lesson_ui("File Operations", lesson_content)
