import psycopg

#keys
from src.config.keys import database, user, host, port, password

class ModelsConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port}  password = {password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_models(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""SELECT * FROM   models;""").fetchall()
            
            models= []
            for emp in data:
                dic = {}
                dic["model_name"] = emp[0]
                dic["brand"] = emp[1]
                dic["type_vehicle"] = emp[2]
                models.append(dic)
            
            return models
    
    def write_model(self, model):
        with self.conn.cursor() as cur:
            cur.execute("""INSERT INTO models(model_name, brand, type_vehicle) VALUES
                        (%(mod_name)s, %(brand)s, %(type_vehicle)s)""", model)
            self.conn.commit()