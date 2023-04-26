import streamlit as st


st.write(os.getcwd())

l = list(os.walk(os.getcwd()))

st.write(l)
