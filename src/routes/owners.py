from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.owners_connection import ownersConnection

owners_router = APIRouter()

conn =ownersConnection()

@owners_router.get("/owners", status_code=HTTP_200_OK)
def read_all_owners():
    return conn.read_all_owners()