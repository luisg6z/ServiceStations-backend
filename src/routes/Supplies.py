from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.Supplies_connection import SuppliesConnection
from src.schemas.supplies_schema import Supplies

Supplies_router = APIRouter()


@Supplies_router.get("/Supplies", status_code=HTTP_200_OK, tags=["Surte"])
def read_all_Supplies():
    conn =SuppliesConnection()
    return conn.read_all_Supplies()

@Supplies_router.post("/supplies/insert", status_code=HTTP_201_CREATED, tags=["Surte"])
def create_supplies(supplies : Supplies):
    conn =SuppliesConnection()
    data = dict(supplies)
    conn.write_Supplies(data)
    return Response(status_code=HTTP_201_CREATED)

@Supplies_router.put("/supplies/update", status_code=HTTP_201_CREATED, tags=["Surte"])
def update_supplies(supplies : Supplies):
    conn =SuppliesConnection()
    data = dict(supplies)
    conn.update_supplies(data)
    return Response(status_code=HTTP_201_CREATED)