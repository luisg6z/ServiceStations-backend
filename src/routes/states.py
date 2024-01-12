from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.states_connection import statesConnection

states_router = APIRouter()

conn =statesConnection()

@states_router.get("/states", status_code=HTTP_200_OK, tags=["Estados"])
def read_all_states():
    return conn.read_all_states()