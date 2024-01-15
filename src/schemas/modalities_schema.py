from pydantic import BaseModel
from typing import Optional

class Modalities(BaseModel):
    modality_id: Optional[int]
    descrpt : str
