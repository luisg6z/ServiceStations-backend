from datetime import date

from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.service_stations_connection import ServiceStationsConnection
from src.schemas.service_stations_schema import ServiceStations

ServiceStations_router = APIRouter()


@ServiceStations_router.get("/service-stations", status_code=HTTP_200_OK, tags=["Estaciones de servicio"])
def read_all_service_stations():
    conn =ServiceStationsConnection()
    return conn.read_all_ServiceStations()

@ServiceStations_router.post("/service-stations/insert", status_code=HTTP_201_CREATED, tags=["Estaciones de servicio"])
def create_service_station( serv_station : ServiceStations):
    conn =ServiceStationsConnection()
    data = dict(serv_station)
    conn.write_ServiceStations(data)
    return Response(status_code=HTTP_201_CREATED)

@ServiceStations_router.put("/service-stations/update", status_code=HTTP_201_CREATED, tags=["Estaciones de servicio"])
def update_service_station( serv_station : ServiceStations):
    conn =ServiceStationsConnection()
    data = dict(serv_station)
    conn.update_service_station(data)
    return Response(status_code=HTTP_201_CREATED)

@ServiceStations_router.delete("/service-stations/delete/{station_rif}", status_code=HTTP_204_NO_CONTENT, tags=["Estaciones de servicio"])
def delete_service_station(station_rif: str):
    conn = ServiceStationsConnection()
    conn.delete_service_station(station_rif)
    return Response(status_code=HTTP_204_NO_CONTENT)

@ServiceStations_router.get("/service-stations/{start_date}/{end_date}", status_code=HTTP_200_OK, tags=["Estaciones de servicio"])
def daily_gas_service_stations(start_date:date, end_date:date):
    conn =ServiceStationsConnection()
    return conn.alert_stations(start_date, end_date)

@ServiceStations_router.get("/service-stations/alert", status_code=HTTP_200_OK, tags=["Estaciones de servicio"])
def alert_service_stations():
    conn =ServiceStationsConnection()
    return conn.alert_stations()