from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.service_stations_connection import ServiceStationsConnection
ServiceStations_router = APIRouter()

conn =ServiceStationsConnection()

@ServiceStations_router.get("/ServiceStations", status_code=HTTP_200_OK)
def read_all_ServiceStations():
    return conn.read_all_ServiceStations()