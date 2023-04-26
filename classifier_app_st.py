import streamlit as st
import numpy as np
import os
from tensorflow.keras.models import load_model
from PIL import Image


c = os.getcwd()

d = os.path.join(c, 'model')

st.write(d)
#Load the pre-trained model
classifier_model = load_model(d)
st.write('nice')
