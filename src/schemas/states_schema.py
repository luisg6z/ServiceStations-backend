from pydantic import BaseModel
from typing import Optional

class States(BaseModel):
    state_id: Optional[int]
    state_name : str
