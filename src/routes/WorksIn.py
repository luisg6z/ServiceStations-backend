from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.WorksIn_connection import  WorksInConnection

WorksIn_router = APIRouter()

conn = WorksInConnection()

@ WorksIn_router.get("/WorksIn", status_code=HTTP_200_OK)
def read_all_WorksIn():
    return conn.read_all_WorksIn()