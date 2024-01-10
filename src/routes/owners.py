from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.owners_connection import OwnersConnection

owners_router = APIRouter()

conn =OwnersConnection()

@owners_router.get("/states", status_code=HTTP_200_OK)
def read_all_owners():
    return conn.read_all_owners()