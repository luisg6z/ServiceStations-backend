from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.Payments_connection import PaymentsConnection
from src.schemas.Payments_schema import Payments

Payments_router = APIRouter()

conn =PaymentsConnection()

@Payments_router.get("/Payments", status_code=HTTP_200_OK)
def read_all_Payments():
    return conn.read_all_Payments()

@Payments_router.post("/Payments/insert", status_code=HTTP_201_CREATED)
def create_Payments(Payments: Payments):
    data = dict(Payments)
    conn.write_Payments(data)
    return Response(status_code=HTTP_201_CREATED)