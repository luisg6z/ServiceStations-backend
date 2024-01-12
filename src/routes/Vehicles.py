from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.Vehicles_connection import VehiclesConnection

Vehicles_router = APIRouter()

conn =VehiclesConnection()

@Vehicles_router.get("/Vehicles", status_code=HTTP_200_OK, tags=["Vehiculos"])
def read_all_Vehicles():
    return conn.read_all_Vehicles()