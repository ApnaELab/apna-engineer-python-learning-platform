import streamlit as st
import sys
from io import StringIO
import contextlib

def mark_lesson_complete(lesson_name):
    """Mark a lesson as complete in the session state and save progress"""
    # Initialize session state if not already done
    if "completed_lessons" not in st.session_state:
        st.session_state.completed_lessons = {}
    
    st.session_state.completed_lessons[lesson_name] = 1
    # Save to file
    import json
    with open("user_progress.json", "w") as f:
        json.dump(st.session_state.completed_lessons, f)
    
    st.success(f"🎉 Congratulations! You've completed the {lesson_name} lesson!")

def check_completion_status(lesson_name):
    """Check if a lesson is marked as complete"""
    # Initialize session state if not already done
    if "completed_lessons" not in st.session_state:
        st.session_state.completed_lessons = {}
    return st.session_state.completed_lessons.get(lesson_name, 0) == 1

def reset_lesson_progress(lesson_name):
    """Reset the progress for a specific lesson"""
    # Initialize session state if not already done
    if "completed_lessons" not in st.session_state:
        st.session_state.completed_lessons = {}
        
    if lesson_name in st.session_state.completed_lessons:
        st.session_state.completed_lessons[lesson_name] = 0
        # Save to file
        import json
        with open("user_progress.json", "w") as f:
            json.dump(st.session_state.completed_lessons, f)
        st.success(f"Progress for {lesson_name} has been reset.")

@contextlib.contextmanager
def capture_output():
    """Capture stdout and stderr for code execution"""
    old_stdout, old_stderr = sys.stdout, sys.stderr
    new_stdout, new_stderr = StringIO(), StringIO()
    sys.stdout, sys.stderr = new_stdout, new_stderr
    yield new_stdout, new_stderr
    sys.stdout, sys.stderr = old_stdout, old_stderr

def execute_code(code_str):
    """Execute the provided code and return the output"""
    with capture_output() as (out, err):
        try:
            exec(code_str)
            output = out.getvalue()
            error = err.getvalue()
            return output, error, None
        except Exception as e:
            return out.getvalue(), err.getvalue(), str(e)

def create_code_executor(default_code=""):
    """Create an interactive code editor with execution capability"""
    # Create a unique ID for this code executor based on the code content
    import hashlib
    unique_id = hashlib.md5(default_code.encode()).hexdigest()[:8]
    
    code = st.text_area("Code Editor", value=default_code, height=200, key=f"editor_{unique_id}")
    
    if st.button("Run Code", key=f"run_{unique_id}"):
        output, error, exception = execute_code(code)
        
        if exception:
            st.error(f"Exception: {exception}")
        
        if error:
            st.error(f"Error: {error}")
        
        if output:
            st.code(output, language="")
            
        return code, output, error, exception
    
    return code, None, None, None

def create_exercise(exercise_prompt, solution_code, test_func=None):
    """Create an interactive exercise with validation"""
    # Create a unique ID for this exercise based on the prompt
    import hashlib
    unique_id = hashlib.md5(exercise_prompt.encode()).hexdigest()[:8]
    
    st.markdown(f"### Exercise: {exercise_prompt}")
    
    user_code = st.text_area("Your Solution", height=200, key=f"exercise_{unique_id}")
    
    if st.button("Check Solution", key=f"check_{unique_id}"):
        if not user_code.strip():
            st.warning("Please write some code before checking.")
            return False
        
        output, error, exception = execute_code(user_code)
        
        if exception or error:
            st.error("Your code has errors. Please fix them and try again.")
            if exception:
                st.error(f"Exception: {exception}")
            if error:
                st.error(f"Error: {error}")
            return False
        
        if test_func:
            # Use a custom testing function if provided
            is_correct = test_func(user_code, output)
        else:
            # Simple solution comparison
            solution_output, _, _ = execute_code(solution_code)
            is_correct = output.strip() == solution_output.strip()
        
        if is_correct:
            st.success("✅ Correct! Great job!")
            return True
        else:
            st.error("❌ Your solution doesn't match the expected output. Try again!")
            return False
    
    return False

def lesson_ui(lesson_title, lesson_content_func):
    """Standard UI wrapper for lessons"""
    st.title(f"🐍 {lesson_title}")
    
    # Check completion status
    is_completed = check_completion_status(lesson_title)
    
    # Display completion badge if completed
    if is_completed:
        st.success(f"✅ You've completed this lesson!")
    
    # Call the lesson content function which should return True if all exercises are passed
    all_passed = lesson_content_func()
    
    # Generate a unique ID for this lesson
    import hashlib
    lesson_id = hashlib.md5(lesson_title.encode()).hexdigest()[:8]
    
    # Add completion button
    if all_passed and not is_completed:
        if st.button("Mark Lesson as Complete", key=f"complete_{lesson_id}"):
            mark_lesson_complete(lesson_title)
            st.rerun()
    
    # Reset progress option
    if is_completed:
        if st.button("Reset Progress for this Lesson", key=f"reset_{lesson_id}"):
            reset_lesson_progress(lesson_title)
            st.rerun()
