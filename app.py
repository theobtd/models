import streamlit as st
import pandas as pd
import pickle

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

st.title("Pest Risk Prediction")

# Input fields
temp_min = st.number_input("Min Temperature")
temp_max = st.number_input("Max Temperature")
humidity = st.number_input("Humidity")
precipitation = st.number_input("Precipitation")

if st.button("Predict"):
    data = pd.DataFrame([[temp_min, temp_max, humidity, precipitation]], 
                        columns=['tempmin_5days', 'tempmax_5days', 'humidity_5days', 'precip_5days'])
    prediction = model.predict(data)
    st.write(f"Risk Level: {prediction[0]}")