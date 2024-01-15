from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.cities_connection import citiesConnection
from src.schemas.cities_schema import Cities

cities_router = APIRouter()

@cities_router.get("/cities", status_code=HTTP_200_OK, tags=["Ciudades"])
def read_cities():
    conn = citiesConnection()
    return conn.read_all_cities()

@cities_router.post("/cities/insert", status_code=HTTP_201_CREATED, tags=["Ciudades"])
def create_city(city : Cities):
    conn = citiesConnection()
    data = dict(city)
    conn.write_cities(data)
    return Response(status_code=HTTP_201_CREATED)

@cities_router.put("/cities/update", status_code=HTTP_201_CREATED, tags=["Ciudades"])
def update_city(city: Cities):
    conn = citiesConnection()
    data = dict(city)
    conn.update_city(data)
    return Response(status_code=HTTP_201_CREATED)

@cities_router.delete("/cities/delete/{city_id}", status_code=HTTP_204_NO_CONTENT, tags=["Ciudades"])
def delete_city(city_id: int):
    conn = citiesConnection()
    conn.delete_city(city_id)
    return Response(status_code=HTTP_204_NO_CONTENT)