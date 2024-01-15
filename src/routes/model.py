from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.model_connection import  ModelsConnection
from src.schemas.model_schema import Models

models_router = APIRouter()


@models_router.get("/models", status_code=HTTP_200_OK, tags=["Modelos"])
def read_all_model():
    conn =ModelsConnection()
    return conn.read_all_models()

@models_router.post("/models/insert", status_code=HTTP_201_CREATED, tags=["Modelos"])
def create_model( model : Models):
    conn =ModelsConnection()
    data = dict(model)
    conn.write_model(data)
    return Response(status_code=HTTP_201_CREATED)

@models_router.put("/models/update", status_code=HTTP_201_CREATED, tags=["Modelos"])
def update_model(model: Models):
    conn = ModelsConnection()
    data = dict(model)
    conn.update_model(data)
    return Response(status_code=HTTP_201_CREATED)