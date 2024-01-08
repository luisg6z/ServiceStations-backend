from pydantic import BaseModel

class States(BaseModel):
    state_id : str
    state_name : str
