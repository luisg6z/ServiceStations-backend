import psycopg

#keys
from src.config.keys import database, user, host, port, password

class modalitiesConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port} password={password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_modalities(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""
                              SELECT
                                modality_id,
                                descrpt
                              FROM modalities;""").fetchall()
            
            modalities = []
            for emp in data:
                dic = {}
                dic["modality_id"] = emp[0]
                dic["descrpt"] = emp[1]
                modalities.append(dic)
            
            return modalities
    
    def write_modalities(self,modalities):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            INSERT INTO modalities(
                                descrpt
                            ) VALUES(
                                %(descrpt)s )""", modalities)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()