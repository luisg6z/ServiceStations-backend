from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.Applies_connection import AppliesConnection
from src.schemas.applies_schema import Applies

Applies_router = APIRouter()

conn = AppliesConnection()

@Applies_router.get("/Applies", status_code=HTTP_200_OK)
def read_all_Applies():
    return conn.read_all_Applies()

@Applies_router.post("/applies/insert", status_code=HTTP_201_CREATED)
def create_applies(applies: Applies):
    data = dict(applies)
    conn.write_applies(data)
    return Response(status_code=HTTP_201_CREATED)