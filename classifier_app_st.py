import streamlit as st
import OS

st.write(os.getcwd())

l = list(os.walk(os.getcwd()))

st.write(l)
