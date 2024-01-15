from pydantic import BaseModel
from typing import Optional

class Cities(BaseModel):
    city_id : Optional[int]
    city_name : str
    state_id : str
