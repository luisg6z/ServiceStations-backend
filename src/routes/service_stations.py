from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.service_stations_connection import ServiceStationsConnection
from src.schemas.service_stations_schema import ServiceStations
ServiceStations_router = APIRouter()

conn =ServiceStationsConnection()

@ServiceStations_router.get("/ServiceStations", status_code=HTTP_200_OK)
def read_all_ServiceStations():
    return conn.read_all_ServiceStations()

@ServiceStations_router.post("/ServiceStations/insert", status_code=HTTP_201_CREATED)
def create_ServiceStations(ServiceStations: ServiceStations):
    data = dict(ServiceStations)
    conn.write_ServiceStations(data)
    return Response(status_code=HTTP_201_CREATED)