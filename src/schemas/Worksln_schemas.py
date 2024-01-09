from pydantic import BaseModel


class WorksIn(BaseModel):
    station_rif: str 
    emp_id  : str
  