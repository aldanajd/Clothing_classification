import streamlit as st
import numpy as np
import os
from tensorflow.keras.models import load_model
from PIL import Image


c = os.getcwd()
f = list(os.walk(os.getcwd()))[0][1]
#d = os.path.join(c, f)
st.write(c)
st.write(f)
#Load the pre-trained model
#classifier_model = load_model(d)
