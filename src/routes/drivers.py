from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.drivers_connection import DriversConnection

drivers_router = APIRouter()

conn = DriversConnection()

@drivers_router.get("/drivers", status_code=HTTP_200_OK)
def read_Drivers():
    return conn.read_all_drivers()