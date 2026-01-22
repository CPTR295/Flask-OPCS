from config.db import connect_db
from typing import Dict, Any
from datetime import date 

@connect_db
def insert_patient_contract(conn,pid:int,approved_by:str,approved_date:date,hcp:str,payment_mode:str,amount_paid:float,amount_due:float):
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO patient_contract (pid,approved_by,approved_date,health_care_provider,payment_mode,amount_paid,amount_due) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        values = (pid,approved_by,approved_date,hcp,payment_mode,amount_paid,amount_due)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error inserting patient contract: {e}")
    return False

@connect_db
def update_patient_contract(conn,id:int,details:Dict[str,Any]):
    try:
        cur = conn.cursor()
        params = ['{}=%s'.format(k) for k in details.keys()]
        values = tuple(details.values())
        sql = 'UPDATE patient_contract SET {} WHERE id=%s'.format(','.join(params),id);
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error updating patient contract: {e}")
    return False

@connect_db
def delete_patient_contract_id(conn,id:int):
    try:
        cur = conn.cursor()
        sql = 'DELETE FROM patient_contract WHERE id=%s'
        values = (id,)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error deleting patient contract: {e}")
    return False

@connect_db
def delete_patient_contract_pid(conn,pid:int):
    try:
        cur = conn.cursor()
        sql = 'DELETE FROM patient_contract WHERE pid=%s'
        values = (pid,)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error deleting patient contract by pid: {e}")
    return False

@connect_db
def select_all_patient_contracts(conn):
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM patient_contract'
        cur.execute(sql)
        results = cur.fetchall()
        cur.close()
        return results
    except Exception as e:
        cur.close()
        print(f"Error selecting all patient contracts: {e}")
    return None 


@connect_db
def select_all_unpaid_patient(conn):
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM patient_contract WHERE amount_due > 0'
        cur.execute(sql)
        results = cur.fetchall()
        cur.close()
        return results
    except Exception as e:
        cur.close()
        print(f"Error selecting all unpaid patient contracts: {e}")
    return None

@connect_db
def select_single_patient_contract(conn,id:int):
    try:
        cur =conn.cursor()
        sql = 'SELECT * FROM patient_contract WHERE id={}'.format(id)
        cur.execute(sql)
        result = cur.fetchone()
        cur.close()
        return result
    except Exception as e:
        cur.close()
        print(f"Error selecting single patient contract: {e}")
    return None