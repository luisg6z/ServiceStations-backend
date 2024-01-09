from pydantic import BaseModel
from datetime import date

class Vehicles(BaseModel):
    plate: str 
    model : str
    capacity : int
    year_release : int
    serial_bodywork : str
    serial_chassis : str
    owner_id: str
  