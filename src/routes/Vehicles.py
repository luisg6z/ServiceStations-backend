from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.Vehicles_connection import VehiclesConnection
from src.schemas.vehicles_schema import Vehicles
from src.schemas.vehicle_dispatch_schema import VehicleDispatch

Vehicles_router = APIRouter()


@Vehicles_router.get("/Vehicles", status_code=HTTP_200_OK, tags=["Vehiculos"])
def read_all_Vehicles():
    conn =VehiclesConnection()
    return conn.read_all_Vehicles()

@Vehicles_router.post("/vehicles/insert", status_code=HTTP_201_CREATED, tags=["Vehiculos"])
def create_vehicle(vehicle : Vehicles):
    conn =VehiclesConnection()
    data = dict(vehicle)
    conn.write_Vehicles(data)
    return Response(status_code=HTTP_201_CREATED)

@Vehicles_router.put("/vehicles/update", status_code=HTTP_201_CREATED, tags=["Vehiculos"])
def update_vehicle(vehicle : Vehicles):
    conn =VehiclesConnection()
    data = dict(vehicle)
    conn.update_vehicle(data)
    return Response(status_code=HTTP_201_CREATED)

@Vehicles_router.delete("/vehicles/delete/{plate}", status_code=HTTP_204_NO_CONTENT, tags=["Vehiculos"])
def delete_vehicle(plate: str):
    conn = VehiclesConnection
    conn.delete_vehicle(plate)
    return Response(status_code=HTTP_204_NO_CONTENT)

@Vehicles_router.get("/Vehicles/dispatch", status_code=HTTP_200_OK, tags=["Vehiculos"])
def vehicles_dispatched(vehicle_dispatch : VehicleDispatch):
    conn =VehiclesConnection()
    return conn.vehicles_dispatched(vehicle_dispatch)