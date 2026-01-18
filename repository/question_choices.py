from config.db import connect_db
from typing import Dict, Any
from datetime import date 

@connect_db 
def insert_question_choice(conn,qid:int,item_id:int,choice:str,choice_text:str,correct_choice:str):
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO question_choice (qid, item_id, choice, choice_text, correct_choice) VALUES (%s, %s, %s, %s, %s)'
        values = (qid, item_id, choice, choice_text, correct_choice)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error inserting question choice: {e}")
    return False

@connect_db
def update_question_choice(conn,id:int,details:Dict[str, Any]):
    try:
        cur = conn.cursor()
        params = ['{}=%s'.format(k) for k in details.keys()] 
        values = tuple(details.values())
        sql = 'UPDATE question_choice SET {} where id = {}'.format(', '.join(params), id)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error updating question choice: {e}")
    return False

@connect_db
def delete_question_choice(conn,id:int):
    try:
        cur = conn.cursor()
        sql = 'DELETE FROM question_choice WHERE id = %s'
        values = (id,)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(f"Error deleting question choice: {e}")
    return False

@connect_db
def select_all_question_choice(conn):
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM question_choice'
        cur.execute(sql)
        results = cur.fetchall()
        cur.close()
        return results
    except Exception as e:
        cur.close()
        print(f"Error selecting all question choices: {e}")
    return None 

@connect_db
def select_single_question_choice(conn,id:int):
    try:
        cur = conn.cursor()
        sql = 'SELECT * FROM question_choice WHERE id = %s'
        values = (id,)
        cur.execute(sql, values)
        result = cur.fetchone()
        cur.close()
        return result
    except Exception as e:
        cur.close()
        print(f"Error selecting single question choice: {e}")
    return None

