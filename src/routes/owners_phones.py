from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.OwnersPhones_connection import OwnersPhonesConnection
OwnersPhones_router = APIRouter()

conn =OwnersPhonesConnection()

@OwnersPhones_router.get("/OwnersPhones", status_code=HTTP_200_OK)
def read_all_OwnersPhones():
    return conn.read_all_OwnersPhones()