from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.employee import employee_router
from src.routes.drivers import drivers_router
from src.routes.tanker_trucks import tankertrucks_router
from src.routes.modalities import modalities_router
from src.routes.states import states_router
from src.routes.owners import owners_router
from src.routes.rates import rates_router
from src.routes.model import models_router
from src.routes.cities import cities_router
from src.routes.service_stations import ServiceStations_router
from src.routes.Vehicles import Vehicles_router
from src.routes.Payments import Payments_router
from src.routes.Dispatched import  Dispatched_router
from src.routes.WorksIn import  WorksIn_router
from src.routes.Supplies import  Supplies_router
from src.routes.Applies import  Applies_router
from src.routes.Drives import  Drives_router
from src.routes.employees_phones import EmployeesPhones_router
from src.routes.owners_phones import OwnersPhones_router

app = FastAPI()

app.include_router(employee_router)
app.include_router(drivers_router)
app.include_router(tankertrucks_router)
app.include_router(modalities_router)
app.include_router(states_router)
app.include_router(owners_router)
app.include_router(rates_router)
app.include_router(models_router)
app.include_router(cities_router)
app.include_router(ServiceStations_router)
app.include_router(Vehicles_router)
app.include_router(Payments_router)
app.include_router(Dispatched_router)
app.include_router(WorksIn_router)
app.include_router(Supplies_router)
app.include_router(Applies_router)
app.include_router(Drives_router)
app.include_router(EmployeesPhones_router)
app.include_router(OwnersPhones_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)