import psycopg

#keys
from src.config.keys import database, user, host, port, password

class  SuppliesConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port}  password = {password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_Supplies(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""SELECT
                              station_rif,
                              plate,
                              supplies_date,
                              liters,
                              driver_id,
                              plateTT
                              FROM  supplies;""").fetchall()
            
            Supplies= []
            for emp in data:
                dic = {}
                dic["station_rif"] = emp[0]
                dic["plate"] = emp[1]
                dic["Supplies_date"]= emp[2]
                dic["liters"] = emp[3]
                dic["driver_id"] = emp[4]
                dic["plateTT"] = emp[5]
                Supplies.append(dic)
            
            return  Supplies
      