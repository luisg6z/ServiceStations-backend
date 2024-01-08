from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.rates_connection import ratesConnection

rates_router = APIRouter()

conn =ratesConnection()

@rates_router.get("/Rates", status_code=HTTP_200_OK)
def read_all_rates():
    return conn.read_all_rates()