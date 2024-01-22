import psycopg

#keys
from src.config.keys import database, user, host, port, password

class  SuppliesConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port}  password = {password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_Supplies(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""
                              SELECT
                                station_rif,
                                supplies_date,
                                liters,
                                driver_id,
                                plateTT
                              FROM  supplies;""").fetchall()
            
            Supplies= []
            for emp in data:
                dic = {}
                dic["station_rif"] = emp[0]
                dic["Supplies_date"]= emp[1]
                dic["liters"] = emp[2]
                dic["driver_id"] = emp[3]
                dic["plateTT"] = emp[4]
                Supplies.append(dic)
            
            return  Supplies
    
    def write_Supplies(self,Supplies):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            INSERT INTO Supplies(
                                station_rif,
                                Supplies_date,
                                liters,
                                driver_id,
                                plateTT
                            ) VALUES(
                                %(station_rif)s,
                                %(Supplies_date)s,
                                %(liters)s,
                                %(driver_id)s,
                                %(plateTT)s )""", Supplies)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
            
    def update_supplies(self, supply):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            UPDATE supplies
                            SET
                            liters = %(liters)s
                            WHERE station_rif = %(station_rif)s AND
                            Supplies_date = %(Supplies_date)s AND
                            plateTT = %(plateTT)s AND
                            driver_id = %(driver_id)s
                            """, supply)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
    
    def delete_supply(self,station_rif, supplies_date, plateTT, driver_id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            DELETE FROM supplies
                            WHERE
                            station_rif = %s AND
                            supplies_date = %s AND
                            plateTT = %s AND
                            driver_id = %s
                            """, (station_rif, supplies_date, plateTT, driver_id))
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()