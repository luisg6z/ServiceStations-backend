from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.employees_phones_connection import EmployeesPhonesConnection
from src.schemas.employees_phones_schema import EmployeesPhones


EmployeesPhones_router = APIRouter()

@EmployeesPhones_router.get("/EmployeesPhones", status_code=HTTP_200_OK, tags=["Telefonos Empleados"])
def read_all_EmployeesPhones():
    conn =EmployeesPhonesConnection()
    return conn.read_all_EmployeesPhones()

@EmployeesPhones_router.post("/EmployeesPhones/insert", status_code=HTTP_201_CREATED, tags=["Telefonos Empleados"])
def create_employee_phone(EmployeesPhones: EmployeesPhones):
    conn =EmployeesPhonesConnection()
    data = dict(EmployeesPhones)
    conn.write_EmployeesPhones(data)
    return Response(status_code=HTTP_201_CREATED)