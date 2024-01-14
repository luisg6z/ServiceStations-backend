from pydantic import BaseModel
from datetime import date

class Supplies(BaseModel):
    station_rif : str
    Supplies_date :date
    liters : float
    driver_id : str
    plateTT : str
  