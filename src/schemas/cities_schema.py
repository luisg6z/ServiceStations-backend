from pydantic import BaseModel

class cities(BaseModel):
    city_id: int
    city_name : str
    state_id : str