from datetime import date

from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.rates_connection import RatesConnection
from src.schemas.rates_schema import Rates

rates_router = APIRouter()


@rates_router.get("/rates", status_code=HTTP_200_OK, tags=["Tasas"])
def read_all_rates():
    conn =RatesConnection()
    return conn.read_all_rates()

@rates_router.post("/rates/insert", status_code=HTTP_201_CREATED, tags=["Tasas"])
def create_rate(rate : Rates):
    conn =RatesConnection()
    data = dict(rate)
    conn.write_rate(data)
    return Response(status_code=HTTP_201_CREATED)

@rates_router.put("/rates/update", status_code=HTTP_201_CREATED, tags=["Tasas"])
def update_rate(rate : Rates):
    conn =RatesConnection()
    data = dict(rate)
    conn.update_rate(data)
    return Response(status_code=HTTP_201_CREATED)

@rates_router.delete("/rates/delete/{rate_date}", status_code=HTTP_204_NO_CONTENT, tags=["Tasas"])
def delete_rate(rate_date: date):
    conn = RatesConnection()
    conn.delete_rate(rate_date)
    return Response(status_code=HTTP_204_NO_CONTENT)