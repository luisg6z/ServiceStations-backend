from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.modalities_connection import modalitiesConnection
from src.schemas.modalities_schema import Modalities

modalities_router = APIRouter()

conn =modalitiesConnection()

@modalities_router.get("/modalities", status_code=HTTP_200_OK)
def read_modalities():
    return conn.read_all_modalities()

@modalities_router.post("/modalities/insert", status_code=HTTP_201_CREATED)
def create_modalities(modalities: Modalities):
    data = dict(modalities)
    conn.write_modalities(data)
    return Response(status_code=HTTP_201_CREATED)