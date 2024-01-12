import psycopg

#keys
from src.config.keys import database, user, host, port, password

class  DispatchedConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port}  password = {password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_Dispatched(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""
                              SELECT 
                                station_rif,
                                plate,
                                liters,
                                dispatch_date,
                                bs
                              FROM dispatched;""").fetchall()
            
            Dispatched= []
            for emp in data:
                dic = {}
                dic["station_rif"] = emp[0]
                dic["plate"] = emp[1]
                dic["dispatch_date"] = emp[2]
                dic["liters"] = emp[3]
                dic["Bs"] = emp[4]
                Dispatched.append(dic)
            
            return Dispatched
      