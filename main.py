# main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import joblib


app = FastAPI()

# serve the Streamlit app as an HTML file
app.mount("/app", StaticFiles(directory="app", html=True), name="app")

# load the pre-trained model
model = joblib.load("saved_model/saved_model.joblib")

# define the input data model
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# define the prediction endpoint
@app.post("/predict", response_model=List[float])
async def predict(data: IrisInput):
    input_data = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]
    prediction = model.predict(input_data)
    pred_prob = model.predict_proba(input_data)
    
    return prediction, pred_prob.max()*100