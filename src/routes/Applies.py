from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.Applies_connection import AppliesConnection

Applies_router = APIRouter()

conn =AppliesConnection()

@Applies_router.get("/Applies", status_code=HTTP_200_OK, tags=["Aplica"])
def read_all_Applies():
    return conn.read_all_Applies()