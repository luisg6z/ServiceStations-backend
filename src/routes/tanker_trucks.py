from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.tankertrucks_connection import tankertrucksConnection

tankertrucks_router = APIRouter()

conn = tankertrucksConnection()

@tankertrucks_router.get("/tankertrucks", status_code=HTTP_200_OK)
def read_tankertrucks():
    return conn.read_all_tankertrucks()