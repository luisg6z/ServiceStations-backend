from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.tanker_trucks_connection import tankertrucksConnection
from src.schemas.tanker_trucks_schema import TankerTrucks

tankertrucks_router = APIRouter()


@tankertrucks_router.get("/tanker-trucks", status_code=HTTP_200_OK, tags=["Camiones Cisterna"])
def read_tanker_trucks():
    conn = tankertrucksConnection()
    return conn.read_all_tankertrucks()

@tankertrucks_router.post("/tanker-trucks/insert", status_code=HTTP_201_CREATED, tags=["Camiones Cisterna"])
def create_tanker_truck(tank_truck : TankerTrucks):
    conn = tankertrucksConnection()
    data = dict(tank_truck)
    conn.write_tankertrucks(data)
    return Response(status_code=HTTP_201_CREATED)

@tankertrucks_router.put("/tanker-trucks/update", status_code=HTTP_201_CREATED, tags=["Camiones Cisterna"])
def update_tanker_truck(tank_truck : TankerTrucks):
    conn = tankertrucksConnection()
    data = dict(tank_truck)
    conn.update_tanker_truck(data)
    return Response(status_code=HTTP_201_CREATED)

@tankertrucks_router.delete("/tanker-trucks/delete/{plateTT}", status_code=HTTP_204_NO_CONTENT, tags=["Camiones Cisterna"])
def delete_tanker_truck(plateTT: str):
    conn = tankertrucksConnection()
    print(plateTT)
    conn.delete_tanker_truck(plateTT)
    return Response(status_code=HTTP_204_NO_CONTENT)