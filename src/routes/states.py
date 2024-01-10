from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.states_connection import statesConnection
from src.schemas.states_schema import States

states_router = APIRouter()

conn =statesConnection()

@states_router.get("/states", status_code=HTTP_200_OK)
def read_all_states():
    return conn.read_all_states()

@states_router.post("/States/insert", status_code=HTTP_201_CREATED)
def create_States(States: States):
    data = dict(States)
    conn.write_States(data)
    return Response(status_code=HTTP_201_CREATED)