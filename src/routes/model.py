from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.model_connection import  modelsConnection

models_router = APIRouter()

conn =modelsConnection()

@models_router.get("/models", status_code=HTTP_200_OK)
def read_all_model():
    return conn.read_all_models()