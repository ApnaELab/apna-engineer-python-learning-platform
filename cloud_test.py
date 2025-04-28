import streamlit as st
import os
import platform
import sys

st.title("Streamlit Cloud Deployment Test")

st.write("## Environment Information")
st.write(f"- Python version: {platform.python_version()}")
st.write(f"- Streamlit version: {st.__version__}")
st.write(f"- Operating system: {platform.system()} {platform.release()}")

st.write("## Environment Variables")
env_vars = {k: v for k, v in os.environ.items() if not k.startswith("_")}
st.write(env_vars)

st.write("## Path Information")
st.write(f"- Current directory: {os.getcwd()}")
st.write(f"- Python path: {sys.path}")

st.success("If you can see this message, your Streamlit app is running successfully on Streamlit Cloud!")

st.write("## Next Steps")
st.write("Once this test app works, update your deployment to use your main app.py file.")