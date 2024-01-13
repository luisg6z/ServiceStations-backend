import psycopg

#keys
from src.config.keys import database, user, host, port, password

class   DrivesConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port}  password = {password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_Drives(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""
                              SELECT
                                driver_id,
                                plateTT
                              FROM drives;""").fetchall()
            
            Drives= []
            for emp in data:
                dic = {}
                dic["driver_id"] = emp[0]
                dic["plateTT"] = emp[1]
                Drives.append(dic)
            
            return  Drives
    
    def write_Drives(self, Drives):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            INSERT INTO Drives(
                                driver_id,
                                plateTT
                            ) VALUES(
                                %(driver_id)s,
                                %(plateTT)s )""", Drives)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()