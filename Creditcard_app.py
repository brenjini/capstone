import numpy as np
import streamlit as st
from PIL import Image
import pickle

loaded_model = pickle.load(open('trained_model.sav', 'rb'))

def run():
    img1 = Image.open('images.jpg')
    st.image(img1, use_column_width=False)
    st.title("Credit Card Approval Prediction using Machine Learning")

run()