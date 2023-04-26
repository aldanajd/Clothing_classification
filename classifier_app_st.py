import streamlit as st
import os 

f = os.getcwd()
st.write(f)

l = list(os.walk(os.getcwd()))

st.write(l)
