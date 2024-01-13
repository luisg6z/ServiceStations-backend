from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.states_connection import statesConnection
from src.schemas.states_schema import States

states_router = APIRouter()


@states_router.get("/states", status_code=HTTP_200_OK, tags=["Estados"])
def read_all_states():
    conn =statesConnection()
    return conn.read_all_states()

@states_router.post("/states/insert", status_code=HTTP_201_CREATED, tags=["Estados"])
def create_state(state : States):
    conn =statesConnection()
    data = dict(state)
    conn.write_states(data)
    return Response(status_code=HTTP_201_CREATED)