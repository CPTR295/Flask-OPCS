from config.db import connect_db
from typing import Dict, Any,List
from datetime import date

@connect_db
def insert_admin(conn,id:int,fname:str,lname:str,age:int,position:str,emp_started:date,emp_status:bool):
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO admin (id, firstname, lastname, age, position, emp_date, emp_status) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        values = (id, fname, lname, age, position, emp_started, emp_status)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error inserting admin: {e}")
    return False

@connect_db
def update_admin(conn,id:int,details:Dict[str,Any]):
    try:
        cur = conn.cursor()
        params = ['{} = %s'.format(key) for key in details.keys()]
        values = tuple(details.values())
        sql = 'UPDATE admin SET {} WHERE id = {}'.format(', '.join(params), id);
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error updating admin: {e}")
    return False

@connect_db
def delete_admin(conn,id:int):
    try:
        cur = conn.cursor()
        sql = 'DELETE FROM admin WHERE id = %s'
        values = (id,)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error deleting admin: {e}")
    return False

@connect_db
def select_all_admin(conn):
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM admin'
        cur.execute(sql)
        admins = cur.fetchall()
        cur.close()
        return admins
    except Exception as e:
        cur.close()
        print(f"Error selecting admins: {e}")
    return None

@connect_db
def select_single_admin(conn,id:int):
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM admin WHERE id = {}'.format(id)
        cur.execute(sql)
        admin = cur.fetchall()
        cur.close()
        return admin
    except Exception as e:
        cur.close()
        print(f"Error selecting admin: {e}")
    return None

@connect_db
def admin_admin_join_user(conn):
    try:
        cur = conn.cursor()
        sql = 'SELECT * from admin a inner join all_user u on a.id = u.id'
        cur.execute(sql)
        results = cur.fetchall()
        cur.close()
        return results
    except Exception as e:
        cur.close()
        print(f"Error joining admin and user: {e}")
    return None


    