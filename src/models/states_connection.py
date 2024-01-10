import psycopg

#keys
from src.config.keys import database, user, host, port, password

class  statesConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port} password={password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_states(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""SELECT * FROM  states;""").fetchall()
            
            states= []
            for emp in data:
                dic = {}
                dic["state_id"] = emp[0]
                dic["state_name"] = emp[1]
                states.append(dic)
            
            return  states