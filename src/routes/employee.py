from fastapi import APIRouter,Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.employee_connection import EmployeeConnection
from src.schemas.employee_schema import Employee

employee_router = APIRouter()

conn = EmployeeConnection()

@employee_router.get("/employee", status_code=HTTP_200_OK)
def read_employees():
    return conn.read_all_employees()

@employee_router.post("/employee/insert", status_code=HTTP_201_CREATED)
def create_employee( employee : Employee):
    data = dict(employee)
    conn.write_employee(data)
    return Response(status_code=HTTP_201_CREATED)