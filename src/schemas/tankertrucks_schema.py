from pydantic import BaseModel

class TankerTrucks(BaseModel):
    plateTT : str
    capacity_lit : str
