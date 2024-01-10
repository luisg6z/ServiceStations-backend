import psycopg

#keys
from src.config.keys import database, user, host, port, password

class tankertrucksConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port} password={password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_tankertrucks(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""SELECT * FROM TankerTrucks;""").fetchall()
            
            tankertrucks = []
            for emp in data:
                dic = {}
                dic["plateTT"] = emp[0]
                dic["capacity_lit"] = emp[1]
                tankertrucks.append(dic)
            
            return tankertrucks
        
        