from pydantic import BaseModel

class Modalities(BaseModel):
    modality_id : str
    descrpt : str
