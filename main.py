from fastapi import FastAPI
from pydantic import BaseModel
import pickle 
import json

# Creates an instance of a FastAPI app that can respond to HTTP requests.
app = FastAPI()


# This defines the expected input structure using Pydantic. 
# The features which our model is going to take from the user and based on it will predict wether the person will be diabetic or not. 

class ModelInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


# Loads a saved machine learning model  from a .sav file using pickle.
diabetes_model = pickle.load(open('diabetes_model_nb.sav', 'rb'))

# This defines a POST API endpoint at /diabetes_prediction.
@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters: ModelInput):
    input_list = [
        input_parameters.Pregnancies,   # It extracts the values from the input and puts them into a list in the order expected by the model.
        input_parameters.Glucose,
        input_parameters.BloodPressure,
        input_parameters.SkinThickness,
        input_parameters.Insulin,
        input_parameters.BMI,
        input_parameters.DiabetesPedigreeFunction,
        input_parameters.Age
    ]


  #  Feeds the input to the model and gets the prediction (0 = Not Diabetic, 1 = Diabetic).



    prediction = diabetes_model.predict([input_list])
    if prediction[0] == 0:
        return {'prediction': 'The person is not diabetic'}
    else:
        return {'prediction': 'The person is diabetic'}

#This is a simple GET endpoint to verify that the API is working.
@app.get("/")
def read_root():
    return {"message": "Welcome to my Diabetes Prediction Application"}
