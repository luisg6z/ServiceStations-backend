from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.drivers_connection import DriversConnection
from src.schemas.drivers_schema import Drivers

drivers_router = APIRouter()


@drivers_router.get("/drivers", status_code=HTTP_200_OK, tags=["Conductores"])
def read_Drivers():
    conn = DriversConnection()
    return conn.read_all_drivers()

@drivers_router.post("/drivers/insert", status_code=HTTP_201_CREATED, tags=["Conductores"])
def create_driver(driver : Drivers):
    conn = DriversConnection()
    data = dict(driver)
    conn.write_driver(data)
    return Response(status_code=HTTP_201_CREATED)

@drivers_router.put("/drivers/update", status_code=HTTP_201_CREATED, tags=["Conductores"])
def update_drivers(drivers: Drivers):
    conn = DriversConnection()
    data = dict(drivers)
    conn.update_driver(data)
    return Response(status_code=HTTP_201_CREATED)