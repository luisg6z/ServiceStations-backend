from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.Supplies_connection import SuppliesConnection
from src.schemas.supplies_schema import Supplies

Supplies_router = APIRouter()

conn =SuppliesConnection()

@Supplies_router.get("/Supplies", status_code=HTTP_200_OK)
def read_all_Supplies():
    return conn.read_all_Supplies()

@Supplies_router.post("/Supplies/insert", status_code=HTTP_201_CREATED)
def create_Supplies(Supplies: Supplies):
    data = dict(Supplies)
    conn.write_Supplies(data)
    return Response(status_code=HTTP_201_CREATED)