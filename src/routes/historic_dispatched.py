from fastapi import APIRouter
from starlette.status import HTTP_200_OK

from src.models.historic_dispatched_connection import HistoricDispatchedConnection

historic_dispatched_router = APIRouter()


@historic_dispatched_router.get("/historic-dispatched", status_code=HTTP_200_OK, tags=["Historico despachos"])
def read_historic_dispatched():
    conn = HistoricDispatchedConnection()
    return conn.read_historic_dispatched()