from fastapi import FastAPI

from src.routes.employee import employee_router

app = FastAPI()

app.include_router(employee_router)