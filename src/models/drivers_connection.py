import psycopg

#keys
from src.config.keys import database, user, host, port, password

class DriversConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port} password={password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_drivers(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""SELECT * FROM Drivers;""").fetchall()
            
            drivers = []
            for emp in data:
                dic = {}
                dic["driver_id"] = emp[0]
                dic["driver_name"] = emp[1]
                drivers.append(dic)
            
            return drivers