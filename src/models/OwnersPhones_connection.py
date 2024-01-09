import psycopg

#keys
from src.config.keys import database, user, host, port, password

class  OwnersPhonesConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_OwnersPhones(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""SELECT * FROM  OwnersPhones ;""").fetchall()
            
            OwnersPhones= []
            for emp in data:
                dic = {}
                dic["owner_id"] = emp[0]
                dic["phone_number_own"] = emp[1]
                OwnersPhones.append(dic)
            
            return OwnersPhones 
      