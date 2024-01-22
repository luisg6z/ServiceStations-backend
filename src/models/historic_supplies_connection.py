import psycopg

#keys
from src.config.keys import database, user, host, port, password

class  HistoricSuppliesConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port}  password = {password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_historic_supplies(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""
                              SELECT
                                station_rif,
                                supplies_date,
                                liters,
                                driver_id,
                                plateTT
                              FROM historic_supplies;""").fetchall()
            
            Supplies= []
            for emp in data:
                dic = {}
                dic["station_rif"] = emp[0]
                dic["Supplies_date"]= emp[1]
                dic["liters"] = emp[2]
                dic["driver_id"] = emp[3]
                dic["plateTT"] = emp[4]
                Supplies.append(dic)
            
            return  Supplies