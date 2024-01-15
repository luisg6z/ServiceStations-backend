from fastapi import APIRouter,Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.employee_connection import EmployeeConnection
from src.schemas.employee_schema import Employee

employee_router = APIRouter()


@employee_router.get("/employee", status_code=HTTP_200_OK, tags=["Empleado"])
def read_employees():
    conn = EmployeeConnection()
    return conn.read_all_employees()

@employee_router.post("/employee/insert", status_code=HTTP_201_CREATED, tags=["Empleado"])
def create_employee( employee : Employee):
    conn = EmployeeConnection()
    data = dict(employee)
    conn.write_employee(data)
    return Response(status_code=HTTP_201_CREATED)

@employee_router.put("/employee/update", status_code=HTTP_201_CREATED, tags=["Empleado"])
def update_employee(employee: Employee):
    conn = EmployeeConnection()
    data = dict(employee)
    conn.update_employee(data)
    return Response(status_code=HTTP_201_CREATED)

@employee_router.delete("/employee/delete/{emp_id}", status_code=HTTP_204_NO_CONTENT, tags=["Empleado"])
def delete_employee(emp_id: str):
    conn = EmployeeConnection()
    conn.delete_employee(emp_id)
    return Response(status_code=HTTP_204_NO_CONTENT)