from pydantic import BaseModel
from datetime import date

class rates(BaseModel):
    rate_date: date
    rates_value : float 