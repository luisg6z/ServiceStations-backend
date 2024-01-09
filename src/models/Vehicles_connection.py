import psycopg

#keys
from src.config.keys import database, user, host, port, password

class  VehiclesConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_Vehicles(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""SELECT * FROM  Vehicles;""").fetchall()
            
            Vehicles= []
            for emp in data:
                dic = {}
                dic["plate"] = emp[0]
                dic["model"] = emp[1]
                dic["capacity"] = emp[2]
                dic["year_release"] = emp[3]
                dic["serial_bodywork "] = emp[4]
                dic["serial_chassis"] = emp[5]
                dic["owner_id"] = emp[6]
                Vehicles.append(dic)
            
            return  Vehicles
      