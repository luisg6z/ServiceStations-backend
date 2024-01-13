from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.Drives_connection import DrivesConnection
from src.schemas.drives_schema import Drives

Drives_router = APIRouter()

@Drives_router.get("/Drives", status_code=HTTP_200_OK, tags=["Manejan"])
def read_all_Drives():
    conn =DrivesConnection()
    return conn.read_all_Drives()

@Drives_router.post("/drives/insert", status_code=HTTP_201_CREATED, tags=["Manejan"])
def create_drives(drives : Drives):
    conn =DrivesConnection()
    data = dict(drives)
    conn.write_Drives(data)
    return Response(status_code=HTTP_201_CREATED)