from pydantic import BaseModel

class Drivers(BaseModel):
    plateTT : str
    capacity_lit : str
