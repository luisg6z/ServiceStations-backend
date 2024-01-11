import psycopg

#keys
from src.config.keys import database, user, host, port, password

class  AppliesConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port} password = {password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_Applies(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""SELECT 
                              modality_id,
                              city_id,
                              aplies_start_date,
                              aplies_end_date
                              FROM applies;""").fetchall()
            
            Applies= []
            for emp in data:
                dic = {}
                dic["modality_id"] = emp[0]
                dic["city_id"] = emp[1]
                dic["aplies_start_date"] = emp[2]
                dic["aplies_End_date"] = emp[3]
                Applies.append(dic)
            
            return Applies
      