from pydantic import BaseModel


class  Drives(BaseModel):
    driver_id: str 
    plateTT : str
  