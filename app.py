import streamlit as st
import pandas as pd
import pickle

# Load the model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit app
st.title("Risk Prediction App")

# Input features
temp_min = st.number_input("Min Temperature")
temp_max = st.number_input("Max Temperature")
average_temp = st.number_input("Average Temperature")
average_humidity = st.number_input("Average Humidity")
total_rain = st.number_input("Total Rainfall")

if st.button("Predict"):
    features = pd.DataFrame({
        'tempmin_5days': [temp_min],
        'tempmax_5days': [temp_max],
        'temp_5days': [average_temp],
        'humidity_5days': [average_humidity],
        'precip_5days': [total_rain]
    })
    prediction = model.predict(features)
    st.write(f"Risk Level: {prediction[0]}")