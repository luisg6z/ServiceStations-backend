import psycopg

#keys
from src.config.keys import database, user, host, port, password

class  WorksInConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_WorksIn(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""SELECT * FROM  WorksIn;""").fetchall()
            
            WorksIn= []
            for emp in data:
                dic = {}
                dic["station_rif"] = emp[0]
                dic["emp_id"] = emp[1]
                WorksIn.append(dic)
            
            return  WorksIn
      