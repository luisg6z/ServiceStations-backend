from fastapi import FastAPI

from src.routes.employee import employee_router
from src.routes.drivers import drivers_router
from src.routes.tankertrucks import tankertrucks_router
from src.routes.modalities import modalities_router
from src.routes.states import states_router
from src.routes.owners import owners_router
from src.routes.rates import rates_router
from src.routes.model import models_router
from src.routes.cities import cities_router

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