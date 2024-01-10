from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.Supplies_connection import SuppliesConnection

Supplies_router = APIRouter()

conn =SuppliesConnection()

@Supplies_router.get("/Supplies", status_code=HTTP_200_OK)
def read_all_Supplies():
    return conn.read_all_Supplies()