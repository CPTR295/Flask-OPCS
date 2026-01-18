from config.db import connect_db
from typing import Dict, Any
from datetime import date 

@connect_db
def insert_signup(conn,user:str,passw:str,utype:str,fname:str,lname:str,cid:str ) -> bool:
    try:
        cur = conn.cursor()
        sql ='INSERT INTO signup (username, password, user_type, firstname, lastname, cid) VALUES (%s, %s, %s, %s, %s, %s)'
        values = (user, passw, utype, fname, lname, cid)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error inserting signup: {e}")
    return False

@connect_db
def update_signup(conn,id:int,details:Dict[str,Any])->bool:
    try:
        cur = conn.cursor()
        params = ['{}=%s'.format(k) for k in details.keys()]
        values = tuple(details.values())
        sql = 'UPDATE signup SET {} WHERE id={}'.format(', '.join(params), id)
        cur.execute(sql, values )
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error updating signup: {e}")
    return False

@connect_db
def delete_signup(conn,id:int)->bool:
    try:
        cur = conn.cursor()
        sql = 'DELETE FROM signup WHERE id=%s'
        cur.execute(sql, (id,))
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error deleting signup: {e}")
    return False

@connect_db
def select_all_signup(conn)->list[Any]:
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM signup'
        cur.execute(sql)
        results = cur.fetchall()
        cur.close()
        return results
    except Exception as e:
        cur.close()
        print(f"Error selecting all signups: {e}")
    return None 


@connect_db
def select_single_signup(conn,id:int)->Any:
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM signup WHERE id=%s'
        cur.execute(sql, (id,))
        result = cur.fetchone()
        cur.close()
        return result
    except Exception as e:
        cur.close()
        print(f"Error selecting single signup: {e}")
    return None