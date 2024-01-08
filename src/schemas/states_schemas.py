from pydantic import BaseModel

class Drivers(BaseModel):
    state_id : str
    state_name : str
