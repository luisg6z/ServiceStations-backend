from pydantic import BaseModel


class drivers(BaseModel):
    driver_id: str 
    plateTT : str
  