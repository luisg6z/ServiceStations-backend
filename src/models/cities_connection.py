import psycopg

#keys
from src.config.keys import database, user, host, port, password

class citiesConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port} password={password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_cities(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""
                              SELECT
                                city_id,
                                city_name,
                                state_id
                              FROM cities;""").fetchall()
            
            cities = []
            for emp in data:
                dic = {}
                dic["city_id"] = emp[0]
                dic["city_name"] = emp[1]
                dic["state_id"] = emp[2]
                cities.append(dic)
            
            return cities
    
    def write_cities(self, cities):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            INSERT INTO cities(
                                city_name,
                                state_id
                            ) VALUES(
                                %(city_name)s,
                                %(state_id)s)""", cities)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()