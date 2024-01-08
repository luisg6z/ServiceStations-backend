from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.employee_connection import EmployeeConnection

employee_router = APIRouter()

conn = EmployeeConnection()

@employee_router.get("/employee", status_code=HTTP_200_OK)
def read_employees():
    return conn.read_all_employees()