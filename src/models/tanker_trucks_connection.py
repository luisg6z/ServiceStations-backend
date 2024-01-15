import psycopg

#keys
from src.config.keys import database, user, host, port, password

class tankertrucksConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port} password = {password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_tankertrucks(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""
                              SELECT
                                plateTT,
                                capacity_lit
                              FROM TankerTrucks;""").fetchall()
            
            tankertrucks = []
            for emp in data:
                dic = {}
                dic["plateTT"] = emp[0]
                dic["capacity_lit"] = emp[1]
                tankertrucks.append(dic)
            
            return tankertrucks
        
    
    def write_tankertrucks(self,tankertrucks):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            INSERT INTO tankertrucks(
                                plateTT,
                                capacity_lit
                            ) VALUES(
                                %(plateTT)s,
                                %(capacity_lit)s )""", tankertrucks)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
            
    def update_tanker_truck(self, truck):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            UPDATE tankertrucks
                            SET
                            capacity_lit = %(capacity_lit)s
                            WHERE plateTT = %(plateTT)s
                            """, truck)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
    
    def delete_tanker_truck(self, plateTT):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            DELETE FROM tankertrucks
                            WHERE
                            plateTT = %s
                            """, (plateTT,))
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()