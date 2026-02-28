#Streamlit app
# app.py
import streamlit as st
import pandas as pd
import pickle

# Load your saved model
# import joblib
# model = joblib.load("rf_model.pkl")

st.title("Student Grade Predictor")

studytime = st.slider("Study Time (1-4)", 1, 4, 2)
failures = st.selectbox("Past Failures", [0, 1, 2, 3])
absences = st.number_input("Absences", 0, 100, 5)
G1 = st.slider("First Period Grade", 0, 20, 10)
G2 = st.slider("Second Period Grade", 0, 20, 10)

if st.button("Predict Final Grade"):
    st.success(f"Predicted Grade: ~{G1*0.3 + G2*0.5 + studytime - failures:.1f}")