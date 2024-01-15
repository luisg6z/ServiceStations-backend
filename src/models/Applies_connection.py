import psycopg

#keys
from src.config.keys import database, user, host, port, password

class  AppliesConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port} password = {password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_Applies(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""
                              SELECT 
                                modality_id,
                                city_id,
                                aplies_start_date,
                                aplies_end_date
                              FROM applies;""").fetchall()
            
            Applies= []
            for emp in data:
                dic = {}
                dic["modality_id"] = emp[0]
                dic["city_id"] = emp[1]
                dic["aplies_start_date"] = emp[2]
                dic["aplies_End_date"] = emp[3]
                Applies.append(dic)
            
            return Applies
    
    def write_applies(self, applies):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            INSERT INTO applies(
                                modality_id,
                                city_id,
                                aplies_start_date,
                                aplies_End_date
                            ) VALUES(
                                %(modality_id)s,
                                %(city_id)s,
                                %(aplies_start_date)s,
                                %(aplies_End_date)s)""", applies)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
    
    def update_applies(self, applies):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            UPDATE applies
                            SET
                            aplies_end_date = %(aplies_End_date)s
                            WHERE modality_id = %(modality_id)s AND
                            city_id = %(city_id)s AND
                            aplies_start_date = %(aplies_start_date)s
                            """, applies)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
        
    def delete_applies(self,modality_id, city_id, aplies_start_date):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            DELETE FROM applies
                            WHERE
                            modality_id = %s AND
                            city_id = %s AND
                            aplies_start_date = %s
                            """, (modality_id, city_id, aplies_start_date))
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()