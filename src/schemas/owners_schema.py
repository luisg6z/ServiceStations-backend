from pydantic import BaseModel

class Owners(BaseModel):
    owner_id: str
    email: str  
    owner_name: str