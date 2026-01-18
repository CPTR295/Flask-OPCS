from config.db import connect_db
from typing import Dict, Any
from datetime import date 

@connect_db
def insert_question_detail(conn,id:int,cid:str,pid:str,exam_date:date,duration:int):
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO question_detail (id, cid, pid, exam_date, duration) VALUES (%s, %s, %s, %s, %s)'
        values = (id, cid, pid, exam_date, duration)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error inserting question detail: {e}")
    return False

@connect_db
def update_question_detail(conn,id:str,details:Dict[str,Any]):
    try:
        cur = conn.cursor()
        params = ['{}=%s'.format(k) for k in details.keys()] 
        values = tuple(details.values())
        sql = 'UPDATE question_detail SET {} WHERE id={}'.format(', '.join(params),id);
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error updating question detail: {e}")
    return False

@connect_db
def delete_question_detail(conn,id:str):
    try:
        cur = conn.cursor()
        sql = 'DELETE FROM question_detail WHERE id=%s'
        values = (id,)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error deleting question detail: {e}")
    return False

@connect_db
def select_all_question_detail(conn):
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM question_detail'
        cur.execute(sql)
        results = cur.fetchall()
        cur.close()
        return results
    except Exception as e:
        cur.close()
        print(f"Error selecting all question details: {e}")
    return None 

@connect_db
def select_single_question_detail(conn,id:str):
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM question_detail WHERE id=%s'
        values = (id,)
        cur.execute(sql, values)
        result = cur.fetchone()
        cur.close()
        return result
    except Exception as e:
        cur.close()
        print(f"Error selecting single question detail: {e}")
    return None

