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

@states_router.put("/states/update", status_code=HTTP_201_CREATED, tags=["Estados"])
def update_state(state : States):
    conn =statesConnection()
    data = dict(state)
    conn.update_states(data)
    return Response(status_code=HTTP_201_CREATED)

@states_router.delete("/states/delete/{state_id}", status_code=HTTP_204_NO_CONTENT, tags=["Estados"])
def delete_state(state_id: int):
    conn = statesConnection()
    conn.delete_state(state_id)
    return Response(status_code=HTTP_204_NO_CONTENT)