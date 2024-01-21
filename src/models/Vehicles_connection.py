import psycopg

#keys
from src.config.keys import database, user, host, port, password

class  VehiclesConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port}  password = {password}")
        except psycopg.OperationalError as err:
            print(err)
            
            #LEER VEHICULOS
    def read_all_Vehicles(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""
                              SELECT
                                plate,
                                model,
                                capacity,
                                year_release,
                                serial_bodywork,
                                serial_chassis,
                                owner_id
                              FROM vehicles;""").fetchall()
            
            Vehicles= []
            for emp in data:
                dic = {}
                dic["plate"] = emp[0]
                dic["model"] = emp[1]
                dic["capacity"] = emp[2]
                dic["year_release"] = emp[3]
                dic["serial_bodywork "] = emp[4]
                dic["serial_chassis"] = emp[5]
                dic["owner_id"] = emp[6]
                Vehicles.append(dic)
            
            return Vehicles

        #CREAR VEHICULO
    def write_Vehicles(self,Vehicles):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            INSERT INTO Vehicles(
                                plate,
                                model,
                                capacity,
                                year_release,
                                serial_bodywork,
                                serial_chassis,
                                owner_id
                            ) VALUES(
                                %(plate)s,
                                %(model)s,
                                %(capacity)s,
                                %(year_release)s,
                                %(serial_bodywork)s,
                                %(serial_chassis)s,
                                %(owner_id)s)""", Vehicles)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
    
        #ACTUALIZAR VEHICULO
    def update_vehicle(self, vehicle):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            UPDATE vehicles
                            SET
                            model = %(model)s,
                            capacity = %(capacity)s,
                            year_release = %(year_release)s,
                            serial_bodywork = %(serial_bodywork)s,
                            serial_chassis = %(serial_chassis)s,
                            owner_id = %(owner_id)s
                            WHERE plate = %(plate)s
                            """, vehicle)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
    
        #BORRAR VEHICULO
    def delete_vehicle(self,plate):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            DELETE FROM vehicles
                            WHERE
                            plate = %s
                            """, (plate,))
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
            
            #VEHICULOS DESPACHADOS POR TIPO, EN RANGO DE FECHAS
    def vehicles_dispatched(self, state_id, city_id, start_date, end_date):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                        SELECT s.station_rif, m.type_vehicle,COUNT(*) AS cantidad
                        FROM vehicles v
                        JOIN models m ON v.model = m.model_name
                        JOIN dispatched as d ON v.plate = d.plate
                        JOIN servicestations s ON d.station_rif = s.station_rif
                        JOIN cities c ON s.city_id = c.city_id
                        JOIN states st ON c.state_id = st.state_id
                        WHERE
                        st.state_id = %s AND
                        c.city_id = %s AND
                        d.dispatch_date BETWEEN %s AND %s
                        GROUP BY s.station_rif, m.type_vehicle;
                        """, (state_id, city_id, start_date, end_date))
            vehicles = []
            for one in data:
                dic = {}
                dic["station_rif"] = one[0]
                dic["type_vehicle"] = one[1]
                dic["quantity"] = one[2]
                vehicles.append(dic)
            
            return vehicles