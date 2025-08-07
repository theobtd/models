import pandas as pd
import pickle
from flask import Flask, request, jsonify

# Load your trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = pd.DataFrame([data])
    prediction = model.predict(features)
    return jsonify({'risk': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)