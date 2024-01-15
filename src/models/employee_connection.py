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
            data =cur.execute("""
                              SELECT
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
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            INSERT INTO employees(
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
                
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
            
    def update_employee(self, employee):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            UPDATE employees
                            SET
                            first_name = %(first_name)s,
                            last_name = %(last_name)s,
                            adress = %(adress)s,
                            email = %(email)s
                            WHERE emp_id = %(emp_id)s
                            """, employee)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
            
    def delete_employee(self,emp_id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            DELETE FROM employees
                            WHERE
                            emp_id = %s
                            """, (emp_id,))
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()