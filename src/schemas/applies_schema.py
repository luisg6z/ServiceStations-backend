from pydantic import BaseModel
from datetime import date

class Applies(BaseModel):
    modality_id: int
    city_id : int
    plies_start_date : date
    aplies_End_date : date