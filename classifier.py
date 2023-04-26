#import os

#l = list(os.walk(os.getcwd()))
#st.write(l)

import streamlit as st

# Set page title
st.set_page_config(page_title="Print Hello")

# Add title to app
st.title("Welcome to My Streamlit App!")

# Print "hello" in Streamlit
st.write("hello")
