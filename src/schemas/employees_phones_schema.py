from pydantic import BaseModel


class EmployeesPhones(BaseModel):
    emp_id: str 
    phone_number_emp : str
  