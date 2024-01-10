from pydantic import BaseModel

class Models(BaseModel):
    mod_name: str
    brand : str
    type_vehicle : str
