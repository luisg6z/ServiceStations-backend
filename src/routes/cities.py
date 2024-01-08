from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.cities_connection import citiesConnection

cities_router = APIRouter()

conn = citiesConnection()

@cities_router.get("/cities", status_code=HTTP_200_OK)
def read_cities():
    return conn.read_all_cities()