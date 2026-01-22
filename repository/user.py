from config.db import connect_db
from typing import Dict, Any
from datetime import date  

@connect_db
def insert_user(conn,id:int,user:str,passw:str,user_approved:date)->bool: 
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO all_user (id, username, password, user_approved) VALUES (%s, %s, %s, %s)'
        values = (id, user, passw, user_approved)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error inserting user: {e}")
    return False

@connect_db
def update_user(conn,id:int,details:Dict[str,Any])->bool:
    try:
        cur = conn.cursor()
        params = ['{}=%s'.format(k) for k in details.keys()]
        values = tuple(details.values())
        sql = 'UPDATE all_user SET {} WHERE id={}'.format(', '.join(params), id)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error updating user: {e}")
    return False

@connect_db
def delete_user(conn,id:int)->bool:
    try:
        cur = conn.cursor()
        sql = 'DELETE FROM all_user WHERE id=%s'
        cur.execute(sql, (id,))
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error deleting user: {e}")
    return False

@connect_db
def select_all_user(conn)->list[Any]:
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM all_user'
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        return result
    except Exception as e:
        cur.close()
        print(f"Error selecting all users: {e}")
    return None 

@connect_db
def select_single_user(conn,id:int)->Any:
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM all_user WHERE id=%s'
        cur.execute(sql, (id,))
        result = cur.fetchone()
        cur.close()
        return result
    except Exception as e:
        cur.close()
        print(f"Error selecting single user: {e}")
    return None

@connect_db
def validate_user(conn,username:str,password:str)->bool:
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM all_user WHERE username=%s AND password=%s'
        cur.execute(sql, (username, password))
        result = cur.fetchone()
        cur.close()
        if len(result or []) > 0:
            return True
    except Exception as e:
        cur.close()
        print(f"Error validating user: {e}")
    return False