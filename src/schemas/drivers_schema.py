from pydantic import BaseModel

class Drivers(BaseModel):
    driver_id : str
    driver_name : str