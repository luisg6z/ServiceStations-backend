from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.modalities_connection import modalitiesConnection

modalities_router = APIRouter()

conn =modalitiesConnection()

@modalities_router.get("/modalities", status_code=HTTP_200_OK, tags=["Modalidades"])
def read_modalities():
    return conn.read_all_modalities()