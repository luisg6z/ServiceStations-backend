import psycopg

#keys
from src.config.keys import database, user, host, port, password

class  DispatchedConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port}  password = {password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_Dispatched(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""
                              SELECT 
                                station_rif,
                                plate,
                                dispatch_date,
                                liters,
                                bs
                              FROM dispatched;""").fetchall()
            
            Dispatched= []
            for emp in data:
                dic = {}
                dic["station_rif"] = emp[0]
                dic["plate"] = emp[1]
                dic["dispatch_date"] = emp[2]
                dic["liters"] = emp[3]
                dic["Bs"] = emp[4]
                Dispatched.append(dic)
            
            return Dispatched
        
    
    def write_dispatch(self, dispatch):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            INSERT INTO dispatched(
                                station_rif,
                                plate,
                                dispatch_date,
                                liters,
                                bs
                            ) VALUES(
                                %(station_rif)s,
                                %(plate)s,
                                %(dispatch_date)s,
                                %(liters)s,
                                %(bs)s);""", dispatch)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
            
    def update_dispatch(self, dispatch):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            UPDATE dispatched
                            SET
                                liters = %(liters)s,
                                bs = %(bs)s
                            WHERE
                                station_rif = %(station_rif)s AND
                                plate = %(plate)s AND
                                dispatch_date = %(dispatch_date)s
                            """, dispatch)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
    
    def delete_dispatch(self,station_rif, plate, dispatch_date):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            DELETE FROM dispatched
                            WHERE
                            station_rif = %s AND
                            plate = %s AND
                            dispatch_date = %s
                            """, (station_rif, plate, dispatch_date))
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()