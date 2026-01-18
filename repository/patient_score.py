from config.db import connect_db
from typing import Dict, Any

@connect_db
def insert_patient_score(conn,pid:int,qid:int,score:float,total:float,status:str,percentage:float):
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO patient_score(pid,qid,score,total,status,percentage) VALUES (%s,%s,%s,%s,%s,%s)' 
        values = (pid,qid,score,total,status,percentage)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error inserting patient score: {e}")
    return False

@connect_db
def update_patient_score(conn,id:int,details:Dict[str, Any]):
    try:
        cur = conn.cursor()
        params = ['{}=%s'.format(k) for k in details.keys()] 
        values = tuple(details.values()) 
        sql = 'UPDATE patient_score SET {} WHERE id=%s'.format(', '.join(params),id);
        cur.execute(sql,values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error updating patient score: {e}")
    return False

@connect_db
def delete_patient_score(conn,id:int):
    try:
        cur=conn.cursor()
        sql='DELETE FROM patient_score WHERE id=%s'
        values=(id,)
        cur.execute(sql,values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error deleting patient score: {e}")
    return False

@connect_db
def select_all_patient_scores(conn):
    try:
        cur=conn.cursor()
        sql='SELECT * FROM patient_score'
        cur.execute(sql)
        results=cur.fetchall()
        cur.close()
        return results
    except Exception as e:
        cur.close()
        print(f"Error selecting all patient scores: {e}")
    return None 

@connect_db
def select_single_patient_score(conn,id:int):
    try:
        cur=conn.cursor()
        sql='SELECT * FROM patient_score WHERE id=%s'
        values=(id,)
        cur.execute(sql,values)
        result=cur.fetchone()
        cur.close()
        return result
    except Exception as e:
        cur.close()
        print(f"Error selecting single patient score: {e}")
    return None