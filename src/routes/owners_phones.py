from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.owners_phones_connection import OwnersPhonesConnection
from src.schemas.owners_phones_schema import OwnersPhones
OwnersPhones_router = APIRouter()

conn =OwnersPhonesConnection()

@OwnersPhones_router.get("/OwnersPhones", status_code=HTTP_200_OK)
def read_all_OwnersPhones():
    return conn.read_all_OwnersPhones()

@OwnersPhones_router.post("/OwnersPhones/insert", status_code=HTTP_201_CREATED)
def create_OwnersPhones(OwnersPhones: OwnersPhones):
    data = dict(OwnersPhones)
    conn.write_OwnersPhones(data)
    return Response(status_code=HTTP_201_CREATED)