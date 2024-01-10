from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.EmployeesPhones_connection import EmployeesPhonesConnection
EmployeesPhones_router = APIRouter()

conn =EmployeesPhonesConnection()

@EmployeesPhones_router.get("/EmployeesPhones", status_code=HTTP_200_OK)
def read_all_EmployeesPhones():
    return conn.read_all_EmployeesPhones()