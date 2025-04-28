# Python Learning Platform

An interactive Python learning platform designed for beginners to learn programming through hands-on, engaging experiences.

## Features

- **Interactive Lessons**: Learn Python through interactive coding exercises
- **Comprehensive Topics**: From Python basics to data visualization and analysis
- **Real-time Code Execution**: Run code directly in the browser and see results instantly
- **Progress Tracking**: Track your learning progress across multiple lessons
- **Visual Learning**: Create visualizations and analyze data interactively

## Lesson Topics

1. **Python Basics**: Introduction, Syntax, Variables, and Comments
2. **Data Types**: Numbers, Strings, and Boolean
3. **Control Flow**: Conditions, Loops, and Decision Making
4. **Functions**: Creating and Using Functions
5. **Data Structures**: Lists, Dictionaries, Tuples, and Sets
6. **File Operations**: Reading and Writing Files
7. **Error Handling**: Try/Except Statements
8. **Data Visualization**: Charts, Graphs and Visual Representations
9. **Data Analysis**: Data Manipulation, Transformation, and Statistical Analysis

## Installation

### Local Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/python-learning-platform.git
   cd python-learning-platform
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements-github.txt
   ```

4. Run the application:
   ```
   streamlit run app.py
   ```

5. Open your browser and navigate to `http://localhost:8501`

### Streamlit Cloud Deployment

For cloud deployment:

1. Fork or push this repository to your GitHub account
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and sign in with GitHub
3. Click "New app" and select this repository
4. Set the main file path to `streamlit_app.py`
5. Click "Deploy"

## Requirements

- Python 3.8 or higher
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).