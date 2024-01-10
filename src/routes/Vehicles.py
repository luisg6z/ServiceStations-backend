from fastapi import APIRouter,Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.Vehicles_connection import VehiclesConnection
from src.schemas.vehicles_schema import Vehicles

Vehicles_router = APIRouter()

conn =VehiclesConnection()

@Vehicles_router.get("/Vehicles", status_code=HTTP_200_OK)
def read_all_Vehicles():
    return conn.read_all_Vehicles()

@Vehicles_router.post("/Vehicles/insert", status_code=HTTP_201_CREATED)
def create_Vehicles(Vehicles: Vehicles):
    data = dict(Vehicles)
    conn.write_Vehicles(data)
    return Response(status_code=HTTP_201_CREATED)