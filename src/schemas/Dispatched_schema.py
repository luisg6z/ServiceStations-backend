from pydantic import BaseModel
from datetime import date
from typing import Optional

class Dispatched(BaseModel):
    station_rif: str
    plate : str 
    dispatch_date : date
    liters : float
    Bs : Optional[float]