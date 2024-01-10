from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.Dispatched_connection import DispatchedConnection

Dispatched_router = APIRouter()

conn =DispatchedConnection()

@Dispatched_router.get("/Dispatched", status_code=HTTP_200_OK)
def read_all_Dispatched():
    return conn.read_all_Dispatched()