from pydantic import BaseModel

# using Pydantic's baseModel class, defining JSON payload input structure. 
# This definition means these are the datatypes accepted for the imput variables. 
# and it will guide the user on what data to supply to the service in order to get a response.

class CreditCardRecord(BaseModel):
    imput1 : float
    imput2 : float
    imput3 : float
    imput4 : float
    imput5 : float
    imput6 : float
    imput7 : float
    imput8 : float
    imput9 : float
    imput10 : float
    





#[17 14 12 10 16 11  9  7 18  4]




    # time: int
    # v1 : float
    # v2 : float
    # v3 : float
    # v4 : float
    # v5 : float
    # v6 : float
    # v7 : float
    # v8 : float
    # v9 : float
    # v10 : float
    # v11 : float
    # v12 : float
    # v13 : float
    # v14 : float
    # v15 : float
    # v16 : float
    # v17 : float
    # v18 : float
    # v19 : float
    # v20 : float
    # v21 : float
    # v22 : float
    # v23 : float
    # v24 : float
    # v25 : float
    # v26 : float
    # v27 : float
    # v28 : float
    # amount: float




# {
#   "time": 534,
#   "v1": 20.7,
#   "v2": 6.71205963,
#   "v3": 0.9645789,
#   "v4": 9.711131486,
#   "v5": 18.9,
#   "v6": 4.97899,
#   "v7": 4.1335321,
#   "v8": 0.69,
#   "v9": 7.00,
#   "v10": 2.78460911,
#   "v11": 56353.123,
#   "v12": 3.833323113,
#   "v13": 34.6783,
#   "v14": 9.82254,
#   "v15": 0.691924927,
#   "v16": -2.3732,
#   "v17": 0.0145653,
#   "v18": 5.475529127,
#   "v19": -0.43743,
#   "v20": 8.40908054,
#   "v21": -6.4004614,
#   "v22": 125.6854,
#   "v23": 0.334089,
#   "v24": 6.37688,
#   "v25": 1.21253234,
#   "v26": 0.904567,
#   "v27": 8.34768,
#   "v28": 73.3256,
#   "amount": 30087600.8
# }