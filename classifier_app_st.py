import streamlit as st

f = os.getcwd()
st.write(f)

l = list(os.walk(os.getcwd()))

st.write(l)
