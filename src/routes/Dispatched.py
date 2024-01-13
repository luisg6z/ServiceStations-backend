from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.Dispatched_connection import DispatchedConnection
from src.schemas.Dispatched_schema import Dispatched

Dispatched_router = APIRouter()



@Dispatched_router.get("/Dispatched", status_code=HTTP_200_OK, tags=["Despachan"])
def read_all_Dispatched():
    conn =DispatchedConnection()
    return conn.read_all_Dispatched()

@Dispatched_router.post("/dispatched/insert", status_code=HTTP_201_CREATED, tags=["Despachan"])
def create_dispatch(dispatch : Dispatched):
    conn =DispatchedConnection()
    data = dict(dispatch)
    conn.write_dispatch(data)
    return Response(status_code=HTTP_201_CREATED)