from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.rates_connection import RatesConnection
from src.schemas.rates_schema import Rates

rates_router = APIRouter()

conn =RatesConnection()

@rates_router.get("/rates", status_code=HTTP_200_OK)
def read_all_rates():
    return conn.read_all_rates()

@rates_router.post("/rates/insert", status_code=HTTP_201_CREATED)
def create_rate(rate : Rates):
    data = dict(rate)
    conn.write_rate(data)
    return Response(status_code=HTTP_201_CREATED)