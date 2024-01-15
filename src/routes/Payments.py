from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.Payments_connection import PaymentsConnection
from src.schemas.Payments_schema import Payments

Payments_router = APIRouter()


@Payments_router.get("/Payments", status_code=HTTP_200_OK, tags=["Pagos"])
def read_all_Payments():
    conn =PaymentsConnection()
    return conn.read_all_Payments()

@Payments_router.post("/payments/insert", status_code=HTTP_201_CREATED, tags=["Pagos"])
def create_payment(payment : Payments):
    conn =PaymentsConnection()
    data = dict(payment)
    conn.write_payment(data)
    return Response(status_code=HTTP_201_CREATED)

@Payments_router.put("/payments/update", status_code=HTTP_201_CREATED, tags=["Pagos"])
def update_payment(payment : Payments):
    conn =PaymentsConnection()
    data = dict(payment)
    conn.update_payment(data)
    return Response(status_code=HTTP_201_CREATED)