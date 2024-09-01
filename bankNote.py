from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements/inputs
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float