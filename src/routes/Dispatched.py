from datetime import date

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

@Dispatched_router.put("/dispatched/update", status_code=HTTP_201_CREATED, tags=["Despachan"])
def update_dispatch(dispatch: Dispatched):
    conn = DispatchedConnection()
    data = dict(dispatch)
    conn.update_dispatch(data)
    return Response(status_code=HTTP_201_CREATED)

@Dispatched_router.delete("/dispatched/delete/{station_rif}/{plate}/{dispatch_date}", status_code=HTTP_204_NO_CONTENT, tags=["Despachan"])
def delete_dispatch(station_rif:str, plate:str, dispatch_date: date):
    conn = DispatchedConnection()
    conn.delete_dispatch(station_rif, plate, dispatch_date)
    return Response(status_code=HTTP_204_NO_CONTENT)