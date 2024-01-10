from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.tankertrucks_connection import tankertrucksConnection
from src.schemas.tankertrucks_schema import TankerTrucks

tankertrucks_router = APIRouter()

conn = tankertrucksConnection()

@tankertrucks_router.get("/tanker-trucks", status_code=HTTP_200_OK)
def read_tankertrucks():
    return conn.read_all_tankertrucks()

@tankertrucks_router.post("/tanker-trucks/insert", status_code=HTTP_201_CREATED)
def create_tabker_truck(tank_truck : TankerTrucks):
    data = dict(tank_truck)
    conn.write_tanker_truck(data)
    return Response(status_code=HTTP_201_CREATED)