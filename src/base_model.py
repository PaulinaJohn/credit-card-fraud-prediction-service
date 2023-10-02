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
