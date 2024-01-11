import psycopg

#keys
from src.config.keys import database, user, host, port, password

class  ServiceStationsConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port}  password = {password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_ServiceStations(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""SELECT
                              station_rif,
                              adress,
                              amount_of_fuel,
                              payment_type,
                              station_name,
                              city_id,
                              manager_id,
                              manager_start_date
                              FROM servicestations;""").fetchall()
            
            ServiceStations= []
            for emp in data:
                dic = {}
                dic["station_rif "] = emp[0]
                dic["adress"] = emp[1]
                dic["amount_of_fuel"] = emp[2]
                dic["payment_type"] = emp[3]
                dic["station_name"] = emp[4]
                dic["city_id "] = emp[5]
                dic["manager_id"] = emp[6]
                dic["manager_start_date"] = emp[7]
                ServiceStations.append(dic)
            
            return  ServiceStations
        
    def write_ServiceStations(self, ServiceStations):
        with self.conn.cursor() as cur:
            cur.execute("""INSERT INTO ServiceStations(
                station_rif,adress,
                amount_of_fuel,
                payment_type,
                station_name,
                city_id,
                manager_id,
                manager_start_date
                ) VALUES(
                    %(station_rif)s,
                    %(adress)s,
                    %(amount_of_fuel)s,
                    %(payment_type)s,
                    %(station_name)s,
                    %(city_id )s,
                    %(manager_id)s,
                    %(manager_start_date)s)""", ServiceStations)
            self.conn.commit()