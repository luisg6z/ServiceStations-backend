from pydantic import BaseModel

class models(BaseModel):
    model_name: str
    brand : str
    type_vehicle : str
