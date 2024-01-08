from pydantic import BaseModel

class owners(BaseModel):
    owner_id: str
    email: str  
    owner_name: str