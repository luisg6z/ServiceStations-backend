from pydantic import BaseModel
from datetime import date

class Dispatched(BaseModel):
    station_rif: str
    plate : str
    dispatch_date : date
    liters : float
    Bs : float