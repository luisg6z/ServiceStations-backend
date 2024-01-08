import psycopg

#keys
from src.config.keys import database, user, host, port, password

class modalitiesConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_modalities(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""SELECT * FROM Modalities;""").fetchall()
            
            modalities = []
            for emp in data:
                dic = {}
                dic["modality_id"] = emp[0]
                dic["descrpt"] = emp[1]
                modalities.append(dic)
            
            return modalities