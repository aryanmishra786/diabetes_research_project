import json
import requests

url = 'http://127.0.0.1:8002/diabetes_prediction'


# This dictionary represents the input values required by our model
input_data_for_model = {
  "Pregnancies": 8,
  "Glucose": 183,
  "BloodPressure": 64,
  "SkinThickness": 0,
  "Insulin": 0,
  "BMI": 23.3,
  "DiabetesPedigreeFunction": 0.672,
  "Age": 32
}

# Send JSON directly using requests' `json=` parameter
response = requests.post(url, json=input_data_for_model)
print(response.text)