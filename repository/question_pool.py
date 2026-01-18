from config.db import connect_db
from typing import Dict, Any
from datetime import date 

@connect_db
def insert_question_pool(conn,qid:int,question:str,type:int):
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO question_pool (qid, question, type) VALUES (%s, %s, %s)' 
        values = (qid, question, type)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error inserting question pool: {e}")
    return False

@connect_db
def update_question_pool(conn,id:int,details:Dict[str,Any]):
    try:
        cur =conn.cursor()
        params =['{}=%s'.format(k) for k in details.keys()] 
        values = tuple(details.values()) 
        sql = 'UPDATE question_pool SET {} WHERE id={}'.format(', '.join(params), id)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error updating question pool: {e}")
    return False

@connect_db
def delete_question_pool(conn,id:int):
    try:
        cur = conn.cursor()
        sql = 'DELETE FROM question_pool WHERE id=%s'
        values = (id,)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error deleting question pool: {e}")
    return False

@connect_db
def select_all_question_pools(conn):
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM question_pool'
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        return rows
    except Exception as e:
        cur.close()
        print(f"Error selecting all question pools: {e}")
    return None  

@connect_db
def select_single_question_pool(conn,id:int):
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM question_pool WHERE id=%s'
        values = (id,)
        cur.execute(sql, values)
        row = cur.fetchone()
        cur.close()
        return row
    except Exception as e:
        cur.close()
        print(f"Error selecting single question pool: {e}")
    return None

@connect_db
def get_current_id(conn):
    try:
        cur = conn.cursor()
        sql = 'SELECT id from question_pool ORDER BY id DESC LIMIT 1'
        cur.execute(sql)
        row = cur.fetchall()
        cur.close()
        return row
    except Exception as e:
        cur.close()
        print(f"Error getting current id: {e}")
    return None