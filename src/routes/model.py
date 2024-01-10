from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.model_connection import  ModelsConnection
from src.schemas.model_schemas import Models

models_router = APIRouter()

conn =ModelsConnection()

@models_router.get("/models", status_code=HTTP_200_OK)
def read_all_model():
    return conn.read_all_models()

@models_router.post("/models/insert", status_code=HTTP_201_CREATED)
def create_model( model : Models):
    data = dict(model)
    conn.write_model(data)
    return Response(status_code=HTTP_201_CREATED)