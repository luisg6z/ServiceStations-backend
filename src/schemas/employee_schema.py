from pydantic import BaseModel

class Employee(BaseModel):
    emp_id : str
    first_name :str
    last_name :str
    adress : str
    email : str