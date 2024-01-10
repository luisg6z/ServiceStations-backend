from pydantic import BaseModel
from datetime import date

class Payments(BaseModel):
    payment_date : date
    amount : float
    payment_type : str
    card_number : str
    bank : str
    currency: str
    station_rif : str
    plate: str
  