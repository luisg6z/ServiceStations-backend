import psycopg

#keys
from src.config.keys import database, user, host, port, password

class OwnersConnection():
    
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect(f"dbname={database} user={user} host={host} port={port} password={password}")
        except psycopg.OperationalError as err:
            print(err)
            
            
    def read_all_owners(self):
        with self.conn.cursor() as cur:
            data =cur.execute("""
                              SELECT
                                owner_id,
                                email,
                                owner_name
                              FROM  owners;""").fetchall()
            
            owners= []
            for emp in data:
                dic = {}
                dic["owner_id"] = emp[0]
                dic["email"] = emp[1]
                dic["owner_name"] = emp[2]
                owners.append(dic)
            
            return  owners
    
    def write_owners(self,owners):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            INSERT INTO owners(
                                owner_id,
                                email,
                                owner_name
                            ) VALUES(
                                %(owner_id)s,
                                %(email)s,
                                %(owner_name)s)""", owners)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close() 
    
    def update_owner(self, owner):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            UPDATE owners
                            SET
                            email = %(email)s,
                            owner_name = %(owner_name)s
                            WHERE owner_id = %(owner_id)s
                            """, owner)
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()
            
    def delete_owner(self,owner_id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                            DELETE FROM owners
                            WHERE
                            owner_id = %s
                            """, (owner_id,))
                self.conn.commit()
        except Exception as ex:
            raise(ex)
        finally:
            self.conn.close()