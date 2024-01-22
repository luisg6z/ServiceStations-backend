from fastapi import APIRouter
from starlette.status import HTTP_200_OK

from src.models.historic_supplies_connection import HistoricSuppliesConnection

historic_supplies_router = APIRouter()


@historic_supplies_router.get("/historic-supplies", status_code=HTTP_200_OK, tags=["Historico Surte"])
def read_historic_supplies():
    conn = HistoricSuppliesConnection()
    return conn.read_historic_supplies()