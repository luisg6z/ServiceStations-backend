from pydantic import BaseModel

class Cities(BaseModel):
    city_id: int
    city_name : str
    state_id : str
