from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.Drives_connection import DrivesConnection
from src.schemas.drives_schema import Drives
Drives_router = APIRouter()

conn =DrivesConnection()

@Drives_router.get("/Drives", status_code=HTTP_200_OK)
def read_all_Drives():
    return conn.read_all_Drives()

@Drives_router.post("/Drives/insert", status_code=HTTP_201_CREATED)
def create_Drives(Drives: Drives):
    data = dict(Drives)
    conn.write_Drives(data)
    return Response(status_code=HTTP_201_CREATED)