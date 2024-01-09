from pydantic import BaseModel
from datetime import date

class ServiceStations(BaseModel):
    station_rif : str
    adress : str
    amount_of_fuel : int
    payment_type : str
    station_name : str
    city_id : int
    manager_id : str 
    manager_start_date : date