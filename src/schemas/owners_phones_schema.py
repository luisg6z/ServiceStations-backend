from pydantic import BaseModel


class OwnersPhones(BaseModel):
    owner_id : str 
    phone_number_own : str
  