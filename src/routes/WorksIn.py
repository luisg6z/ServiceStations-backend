from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.WorksIn_connection import  WorksInConnection
from src.schemas.worksln_schema import WorksIn

WorksIn_router = APIRouter()

@WorksIn_router.get("/WorksIn", status_code=HTTP_200_OK, tags=["Trabaja en"])
def read_all_WorksIn():
    conn = WorksInConnection()
    return conn.read_all_WorksIn()

@WorksIn_router.post("/worksin/insert", status_code=HTTP_201_CREATED, tags=["Trabaja en"])
def create_works_in(works_in : WorksIn):
    conn = WorksInConnection()
    data = dict(works_in)
    conn.write_WorksIn(data)
    return Response(status_code=HTTP_201_CREATED)