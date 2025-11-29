import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("Student Performance Prediction App")
st.write("Predict Math Score based on Student Information")

# Input fields
gender = st.selectbox("Gender", ["female", "male"])
lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
test_prep = st.selectbox("Test Preparation Course", ["none", "completed"])
reading = st.number_input("Reading Score", 0, 100)
writing = st.number_input("Writing Score", 0, 100)

# Convert input to model-friendly format
data = {
    "reading score": [reading],
    "writing score": [writing],
    "gender_male": [1 if gender == "male" else 0],
    "lunch_standard": [1 if lunch == "standard" else 0],
    "test preparation course_none": [1 if test_prep == "none" else 0]
}

input_df = pd.DataFrame(data)

# Predict
if st.button("Predict Math Score"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Math Score: {round(prediction)}")
