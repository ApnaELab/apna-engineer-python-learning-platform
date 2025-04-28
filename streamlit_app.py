import streamlit as st
import os
import sys
import importlib.util
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(levelname)s - %(message)s')

# Log system information
logging.info(f"Python version: {sys.version}")
logging.info(f"Current directory: {os.getcwd()}")
logging.info(f"Directory contents: {os.listdir('.')}")
logging.info(f"Environment variables: PORT={os.environ.get('PORT', 'Not set')}")

# Set PORT environment variable if not set
if "PORT" in os.environ:
    port = int(os.environ.get("PORT", 8501))
    logging.info(f"Using PORT from environment: {port}")
else:
    port = 8501
    logging.info(f"Using default PORT: {port}")

try:
    # Import the main app.py module
    logging.info("Attempting to import app.py")
    spec = importlib.util.spec_from_file_location("app", "app.py")
    if spec is None:
        logging.error("Failed to create module spec for app.py")
        st.error("Failed to load application: Could not locate app.py")
        raise ImportError("Could not locate app.py")
    
    app = importlib.util.module_from_spec(spec)
    sys.modules["app"] = app
    
    if spec.loader is None:
        logging.error("Module spec has no loader")
        st.error("Failed to load application: Module spec has no loader")
        raise ImportError("Module spec has no loader")
        
    spec.loader.exec_module(app)
    logging.info("Successfully imported app.py")
except Exception as e:
    logging.error(f"Error importing app.py: {e}")
    st.error(f"Error loading application: {e}")
    raise

# Run the app
if __name__ == "__main__":
    logging.info("Starting Streamlit application")
    # The app is already imported and will run through streamlit
    pass