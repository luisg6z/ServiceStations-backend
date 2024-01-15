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
    
    def update_city(self, city):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            UPDATE cities
                            SET
                            city_name = %(city_name)s
                            WHERE city_id = %(city_id)s
                            """, city)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
    
    def delete_city(self,city_id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            DELETE FROM city
                            WHERE
                            city_id = %s
                            """, (city_id,))
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()