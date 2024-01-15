import psycopg

#keys
from src.config.keys import database, user, host, port, password

class DriversConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port} password={password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_drivers(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""
                              SELECT
                                driver_id,
                                driver_name
                              FROM drivers;""").fetchall()
            
            drivers = []
            for emp in data:
                dic = {}
                dic["driver_id"] = emp[0]
                dic["driver_name"] = emp[1]
                drivers.append(dic)
            
            return drivers
    
    def write_driver(self, driver):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            INSERT INTO drivers(
                                driver_id,
                                driver_name
                            ) VALUES(
                                %(driver_id)s,
                                %(driver_name)s)""", driver)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
            
    def update_driver(self, driver):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            UPDATE drivers
                            SET
                            driver_name = %(driver_name)s
                            WHERE driver_id = %(driver_id)s
                            """, driver)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
    
    def delete_driver(self, driver_id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            DELETE FROM drivers
                            WHERE
                            driver_id = %s
                            """, (driver_id,))
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()