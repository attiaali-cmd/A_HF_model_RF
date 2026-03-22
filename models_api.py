import pickle
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ModelInput(BaseModel):
    serum_creatinine: float
    ejection_fraction: int
    age: int

model = pickle.load(open("randomforest.sav", "rb"))

@app.post("/Heart_failure_survival")
def predict(data: ModelInput):
    input_list = [
        data.serum_creatinine,
        data.ejection_fraction,
        data.age
    ]

    prediction = model.predict([input_list])

    if prediction[0] == 1:
        return {"result": "Will Survive"}
    else:
        return {"result": "Will Not Survive"}
