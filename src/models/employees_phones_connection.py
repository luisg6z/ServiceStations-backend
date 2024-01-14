import psycopg

#keys
from src.config.keys import database, user, host, port, password

class  EmployeesPhonesConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port}  password = {password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_EmployeesPhones(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""
                              SELECT
                                emp_id,
                                phone_number_emp
                              FROM  employeesphones ;""").fetchall()
            
            EmployeesPhones= []
            for emp in data:
                dic = {}
                dic["emp_id"] = emp[0]
                dic["phone_number_emp"] = emp[1]
                EmployeesPhones.append(dic)
            
            return EmployeesPhones
        
    def write_EmployeesPhones(self, EmployeesPhones):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            INSERT INTO employeesphones(
                                emp_id,
                                phone_number_emp
                            )VALUES(
                                %(emp_id)s,
                                %(phone_number_emp)s);""", EmployeesPhones)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()