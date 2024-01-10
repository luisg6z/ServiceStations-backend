from fastapi import APIRouter,Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.WorksIn_connection import  WorksInConnection
from src.schemas.worksln_schema import WorksIn

WorksIn_router = APIRouter()

conn = WorksInConnection()

@ WorksIn_router.get("/WorksIn", status_code=HTTP_200_OK)
def read_all_WorksIn():
    return conn.read_all_WorksIn()

@WorksIn_router.post("/WorksIn/insert", status_code=HTTP_201_CREATED)
def create_Vehicles(WorksIn: WorksIn):
    data = dict(WorksIn)
    conn.write_WorksIn(data)
    return Response(status_code=HTTP_201_CREATED)