import psycopg

#keys
from src.config.keys import database, user, host, port, password

class  WorksInConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port}  password = {password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_WorksIn(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""
                              SELECT
                                station_rif,
                                emp_id
                              FROM  worksIn;""").fetchall()
            
            WorksIn= []
            for emp in data:
                dic = {}
                dic["station_rif"] = emp[0]
                dic["emp_id"] = emp[1]
                WorksIn.append(dic)
            
            return  WorksIn
    
    def write_WorksIn(self,WorksIn):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            INSERT INTO WorksIn(
                                station_rif,
                                emp_id
                            ) VALUES(
                                %(station_rif)s,
                                %(emp_id)s )""", WorksIn)
                self.conn.commit()
                
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
    
    def delete_works_in(self,emp_id, station_rif):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            DELETE FROM worksin
                            WHERE
                            emp_id = %s AND
                            station_rif = %s
                            """, (emp_id, station_rif))
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()