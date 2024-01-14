from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.service_stations_connection import ServiceStationsConnection
from src.schemas.service_stations_schema import ServiceStations

ServiceStations_router = APIRouter()


@ServiceStations_router.get("/ServiceStations", status_code=HTTP_200_OK, tags=["Estaciones de servicio"])
def read_all_service_stations():
    conn =ServiceStationsConnection()
    return conn.read_all_ServiceStations()

@ServiceStations_router.post("/service-stations/insert", status_code=HTTP_201_CREATED, tags=["Estaciones de servicio"])
def create_service_station( serv_station : ServiceStations):
    conn =ServiceStationsConnection()
    data = dict(serv_station)
    conn.write_ServiceStations(data)
    return Response(status_code=HTTP_201_CREATED)