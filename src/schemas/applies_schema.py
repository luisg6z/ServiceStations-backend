from pydantic import BaseModel
from datetime import date

class Applies(BaseModel):
    modality_id: int
    city_id: int
    aplies_start_date: date  
    aplies_End_date: date   
