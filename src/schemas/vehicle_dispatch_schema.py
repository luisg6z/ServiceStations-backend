from datetime import date

from pydantic import BaseModel

class VehicleDispatch(BaseModel):
    city_id: int
    state_id : int
    start_date: date
    end_date : date