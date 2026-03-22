import pickle
from fastapi import FastAPI
import json 
from pydantic import BaseModel
from pyngrok import ngrok
import nest_asyncio
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
app=FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class model_input(BaseModel):
    serum_creatinine: float
    ejection_fraction : int
    age :int 
# loading the model 
random_forest = pickle.load(open(r"E:\ibm machine learning\python_files\randomforest.sav", 'rb'))
@app.post('/Heart_failure_survival')
def heart_failure_survival(input_param:model_input):
    input_data=input_param.json()
    input_dictionary = json.loads(input_data)
    scr=input_dictionary['serum_creatinine']
    ef=input_dictionary['ejection_fraction']
    age=input_dictionary['age']
    input_list=[scr,ef,age]
    prediction=random_forest.predict([input_list])
    if prediction[0]==1:
        return 'Will Not Survive'
    else:
        return 'Will Survive'
ngrok.set_auth_token("3BGK2s0E6ZDY3q5D9oOtHKHGbX7_2Ld6o3ZyHN2UaZ4xBaHgk")
ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
    