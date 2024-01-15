import psycopg

#keys
from src.config.keys import database, user, host, port, password

class RatesConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port} password={password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_rates(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""
                              SELECT
                                rate_date,
                                rates_value
                              FROM  rates;""").fetchall()
            
            rates= []
            for emp in data:
                dic = {}
                dic["rate_date"] = emp[0]
                dic["rates_value"] = emp[1]
                rates.append(dic)
            
            return rates
    
    def write_rate(self, rate):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            INSERT INTO rates(
                                rate_date,
                                rates_value
                            ) VALUES(
                                %(rate_date)s,
                                %(rates_value)s)""", rate)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
    
    def update_rate(self, rate):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            UPDATE rates
                            SET
                            rates_value = %(rates_value)s
                            WHERE rate_date = %(rate_date)s
                            """, rate)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()