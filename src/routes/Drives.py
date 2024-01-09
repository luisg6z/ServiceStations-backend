from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.Drives_connection import DrivesConnection
Drives_router = APIRouter()

conn =DrivesConnection()

@Drives_router.get("/Drives", status_code=HTTP_200_OK)
def read_all_Drives():
    return conn.read_all_Drives()