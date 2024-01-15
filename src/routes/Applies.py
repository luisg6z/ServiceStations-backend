from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.Applies_connection import AppliesConnection
from src.schemas.applies_schema import Applies

Applies_router = APIRouter()


@Applies_router.get("/Applies", status_code=HTTP_200_OK, tags=["Aplica"])
def read_all_Applies():
    conn =AppliesConnection()
    return conn.read_all_Applies()

@Applies_router.post("/applies/insert", status_code=HTTP_201_CREATED, tags=["Aplica"])
def create_applies(applies : Applies):
    conn =AppliesConnection()
    data = dict(applies)
    conn.write_applies(data)
    return Response(status_code=HTTP_201_CREATED)

@Applies_router.put("/applies/update", status_code=HTTP_201_CREATED, tags=["Aplica"])
def update_drivers(applies: Applies):
    conn = AppliesConnection()
    data = dict(applies)
    conn.update_applies(data)
    return Response(status_code=HTTP_201_CREATED)