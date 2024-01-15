from fastapi import APIRouter, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.models.owners_phones_connection import OwnersPhonesConnection
from src.schemas.owners_phones_schema import OwnersPhones

OwnersPhones_router = APIRouter()

@OwnersPhones_router.get("/OwnersPhones", status_code=HTTP_200_OK, tags=["Telefonos Dueños"])
def read_all_OwnersPhones():
    conn =OwnersPhonesConnection()
    return conn.read_all_OwnersPhones()

@OwnersPhones_router.post("/OwnersPhones/insert", status_code=HTTP_201_CREATED, tags=["Telefonos Dueños"])
def create_OwnersPhones(OwnersPhones: OwnersPhones):
    conn =OwnersPhonesConnection()
    data = dict(OwnersPhones)
    conn.write_OwnersPhones(data)
    return Response(status_code=HTTP_201_CREATED)

@OwnersPhones_router.delete("/owners-phones/delete/{own_id}/{phone_number_own}", status_code=HTTP_204_NO_CONTENT, tags=["Telefonos Dueños"])
def delete_owner_phone(own_id: str, phone_number_own: str):
    conn = OwnersPhonesConnection()
    conn.delete_employee_phone(own_id, phone_number_own)
    return Response(status_code=HTTP_204_NO_CONTENT)