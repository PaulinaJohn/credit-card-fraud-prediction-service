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

    # time = (float(data.time))
    # v1 = data.v1
    # v2 = data.v2
    # v3 = data.v3
    # v4 = data.v4
    # v5 = data.v5
    # v6 = data.v6
    # v7 = data.v7
    # v8 = data.v8
    # v9 = data.v9
    # v10 = data.v10
    # v11 = data.v11
    # v12 = data.v12
    # v13 = data.v13
    # v14 = data.v14
    # v15 = data.v15
    # v16 = data.v16
    # v17 = data.v17
    # v18 = data.v18
    # v19 = data.v19
    # v20 = data.v20
    # v21 = data.v21
    # v22 = data.v22
    # v23 = data.v23
    # v24 = data.v24
    # v25 = data.v25
    # v26 = data.v26
    # v27 = data.v27
    # v28 = data.v28
    # amount= data.amount

    # Storing variables in list for model prediction
    # variables = [time, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, amount]

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
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# @app.get("/classify_transaction/")
# async def classify_transaction(description: str = Query(..., description="The transaction description")):
#     try:
#         response = perform_classification(description, pipeline)
#         return response
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")