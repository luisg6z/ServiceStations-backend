from pydantic import BaseModel

class Models(BaseModel):
    model_name: str
    brand : str
    type_vehicle : str
