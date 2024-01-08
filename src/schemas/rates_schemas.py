from pydantic import BaseModel
from datetime import date

class Rates(BaseModel):
    rate_date: date
    rates_value : float 
