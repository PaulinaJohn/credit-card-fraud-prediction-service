import joblib
from fastapi import FastAPI, HTTPException #Query
from src.base_model import CreditCardRecord
import os


model = joblib.load('model/model_v1.joblib')

app = FastAPI()

# @app.get("/")
# async def read_service_root():
#      return {"Hello": f"from {os.getenv('ENV', 'DEFAULT_ENV')}"}
     

@app.post("/creditcard_fraud-predictor")
async def check_card_transaction(data: CreditCardRecord):

    # Extracting each variable from CreditCardRecord class.
    V17 = data.imput1
    V14 = data.imput2
    V12 = data.imput3
    V10 = data.imput4
    V16 = data.imput5
    V11 = data.imput6
    V9 = data.imput7
    V7 = data.imput8
    V18 = data.imput9
    V4 = data.imput10

    variables = [V17, V14, V12, V10, V16, V11, V9, V7, V18, V4]
    # Passing variables into saved model for prediction. Remember to pass the variables in the right shape.

    try:
        result = model.predict([variables])
        
        # Formatting result
        if result[0] == 0:
                status = "Not Fraudulent"
        else:
            status = "Fraudulent"

        # Defining output payload
        json_response = {
            "Prediction": str(result[0]),
            "Result": status
        }

        return json_response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")
