from pydantic import BaseModel
from datetime import date
from typing import Optional

class Payments(BaseModel):
    payment_id : Optional[str]
    payment_date : date
    amount : float
    payment_type : str
    card_number : Optional[str]
    bank : Optional[str]
    currency: str
    station_rif : str
    plate: str
  