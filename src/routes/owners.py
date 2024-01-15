from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.owners_connection import OwnersConnection
from src.schemas.owners_schema import Owners

owners_router = APIRouter()


@owners_router.get("/owners", status_code=HTTP_200_OK, tags=["Propietarios"])
def read_all_owners():
    conn =OwnersConnection()
    return conn.read_all_owners()

@owners_router.post("/owners/insert", status_code=HTTP_201_CREATED, tags=["Propietarios"])
def create_owners(owners : Owners):
    conn =OwnersConnection()
    data = dict(owners)
    conn.write_owners(data)
    return Response(status_code=HTTP_201_CREATED)

@owners_router.put("/owners/update", status_code=HTTP_201_CREATED, tags=["Propietarios"])
def update_owner(owner: Owners):
    conn = OwnersConnection()
    data = dict(owner)
    conn.update_owner(data)
    return Response(status_code=HTTP_201_CREATED)

@owners_router.delete("/owners/delete/{owner_id}", status_code=HTTP_204_NO_CONTENT, tags=["[Propietarios]"])
def delete_owners(owner_id: str):
    conn = OwnersConnection
    conn.delete_owner(owner_id)
    return Response(status_code=HTTP_204_NO_CONTENT)