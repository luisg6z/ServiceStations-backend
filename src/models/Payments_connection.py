import psycopg

#keys
from src.config.keys import database, user, host, port, password

class  PaymentsConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port}  password = {password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_Payments(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""SELECT
                              payment_id,
                              payment_date,
                              amount,
                              payment_type,
                              card_number,
                              bank,
                              currency,
                              station_rif,
                              plate
                              FROM  payments;""").fetchall()
            
            Payments= []
            for emp in data:
                dic = {}
                dic["payment_id"] = emp[0]
                dic["payment_date"] = emp[1]
                dic["amount"] = emp[2]
                dic["payment_type"] = emp[3]
                dic["card_number"] = emp[4]
                dic["bank"] = emp[5]
                dic["currency"] = emp[6]
                dic["station_rif"] = emp[7]
                dic["plate"] = emp[8]
                Payments.append(dic)
            
            return Payments
    
    def write_Payments(self, Payments):
        with self.conn.cursor() as cur:
            cur.execute("""INSERT INTO Payments(
                payment_id,
                payment_date,
                amount,
                payment_type,
                card_number,
                bank,
                currency,
                station_rif,
                plate
                ) VALUES(
                    %(payment_id)s,
                    %(payment_date)s,
                    %(amount)s,
                    %(payment_type)s,
                    %(card_number)s,
                    %(bank)s
                    %(currency)s,
                    %(station_rif)s,
                    %(plate)s)""", Payments)
            self.conn.commit()