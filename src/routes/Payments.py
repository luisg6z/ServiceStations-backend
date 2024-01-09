from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.Payments_connection import PaymentsConnection

Payments_router = APIRouter()

conn =PaymentsConnection()

@Payments_router.get("/Payments", status_code=HTTP_200_OK)
def read_all_Payments():
    return conn.read_all_Payments()