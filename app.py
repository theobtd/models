import streamlit as st
import pandas as pd
import pickle
from flask import Flask, request, jsonify

# Load your trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Create a Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from POST request
    data = request.json
    features = pd.DataFrame([data])
    
    # Make predictions using the model
    prediction = model.predict(features)
    
    # Return the prediction as JSON
    return jsonify({'risk': prediction[0]})

# Streamlit app
def main():
    st.title("Risk Prediction App")
    
    # Input features
    temp_min = st.number_input("Min Temperature")
    temp_max = st.number_input("Max Temperature")
    average_temp = st.number_input("Average Temperature")
    average_humidity = st.number_input("Average Humidity")
    total_rain = st.number_input("Total Rainfall")

    if st.button("Predict"):
        features = {
            'tempmin_5days': temp_min,
            'tempmax_5days': temp_max,
            'temp_5days': average_temp,
            'humidity_5days': average_humidity,
            'precip_5days': total_rain
        }

        # Call the API for prediction
        response = requests.post('http://localhost:5000/predict', json=features)
        prediction = response.json().get('risk')
        st.write(f"Risk Level: {prediction}")

if __name__ == '__main__':
    # Run the Flask app in a separate thread
    from threading import Thread
    Thread(target=app.run, kwargs={'port': 5000}).start()
    
    # Run the Streamlit app
    main()