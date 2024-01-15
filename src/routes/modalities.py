from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.modalities_connection import modalitiesConnection
from src.schemas.modalities_schema import Modalities

modalities_router = APIRouter()


@modalities_router.get("/modalities", status_code=HTTP_200_OK, tags=["Modalidades"])
def read_modalities():
    conn =modalitiesConnection()
    return conn.read_all_modalities()

@modalities_router.post("/modalities/insert", status_code=HTTP_201_CREATED, tags=["Modalidades"])
def create_modality(modality : Modalities):
    conn =modalitiesConnection()
    data = dict(modality)
    conn.write_modalities(data)
    return Response(status_code=HTTP_201_CREATED)

@modalities_router.put("/modalities/update", status_code=HTTP_201_CREATED, tags=["Modalidades"])
def update_modality(modality: Modalities):
    conn = modalitiesConnection()
    data = dict(modality)
    conn.update_modality(data)
    return Response(status_code=HTTP_201_CREATED)

@modalities_router.delete("/modalities/delete/{modality_id}", status_code=HTTP_204_NO_CONTENT, tags=["Modalidades"])
def update_modality(modality_id: int):
    conn = modalitiesConnection()
    conn.delete_modality()
    return Response(status_code=HTTP_204_NO_CONTENT)