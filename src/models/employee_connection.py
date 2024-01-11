import psycopg

#keys
from src.config.keys import database, user, host, port, password

class EmployeeConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port} password={password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_employees(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""SELECT
                              emp_id,
                              first_name,
                              last_name,
                              adress,
                              email
                              FROM employees;""").fetchall()
            
            employees = []
            for emp in data:
                dic = {}
                dic["emp_id"] = emp[0]
                dic["first_name"] = emp[1]
                dic["last_name"] = emp[2]
                dic["adress"] = emp[3]
                dic["email"] = emp[4]
                employees.append(dic)
            
            return employees
        
    def write_employee(self, employee):
        with self.conn.cursor() as cur:
            cur.execute("""INSERT INTO employees(
                emp_id,
                first_name,
                last_name,
                adress, 
                email
                ) VALUES(
                    %(emp_id)s,
                    %(first_name)s,
                    %(last_name)s,
                    %(adress)s,
                    %(email)s);""", employee)
            
            cur.execute("""INSERT INTO EmployeesPhones(
                emp_id,
                phone_number_emp
                ) VALUES(
                    %(emp_id)s,
                    %(phone)s)""", employee)
            self.conn.commit()