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
            data =cur.execute("""SELECT * FROM  Rates;""").fetchall()
            
            rates= []
            for emp in data:
                dic = {}
                dic["rate_date"] = emp[0]
                dic["rates_value"] = emp[1]
                rates.append(dic)
            
            return  rates