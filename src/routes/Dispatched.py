from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.Dispatched_connection import DispatchedConnection
from src.schemas.Dispatched_schema import Dispatched

Dispatched_router = APIRouter()

conn =DispatchedConnection()

@Dispatched_router.get("/Dispatched", status_code=HTTP_200_OK)
def read_all_Dispatched():
    return conn.read_all_Dispatched()

@Dispatched_router.post("/Dispatched/insert", status_code=HTTP_201_CREATED)
def create_Dispatched(Dispatched: Dispatched):
    data = dict(Dispatched)
    conn.write_Dispatched(data)
    return Response(status_code=HTTP_201_CREATED)