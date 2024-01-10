from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.EmployeesPhones_connection import EmployeesPhonesConnection
from src.schemas.employees_phones_schema import EmployeesPhones


EmployeesPhones_router = APIRouter()

conn =EmployeesPhonesConnection()

@EmployeesPhones_router.get("/EmployeesPhones", status_code=HTTP_200_OK)
def read_all_EmployeesPhones():
    return conn.read_all_EmployeesPhones()

@EmployeesPhones_router.post("/EmployeesPhones/insert", status_code=HTTP_201_CREATED)
def create_applies(EmployeesPhones: EmployeesPhones):
    data = dict(EmployeesPhones)
    conn.write_EmployeesPhones(data)
    return Response(status_code=HTTP_201_CREATED)