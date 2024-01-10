from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.cities_connection import citiesConnection
from src.schemas.cities_schema import Cities

cities_router = APIRouter()

conn = citiesConnection()

@cities_router.get("/cities", status_code=HTTP_200_OK)
def read_cities():
    return conn.read_all_cities()

@cities_router.post("/cities/insert", status_code=HTTP_201_CREATED)
def create_cities(cities: Cities):
    data = dict(cities)
    conn.write_cities(data)
    return Response(status_code=HTTP_201_CREATED)