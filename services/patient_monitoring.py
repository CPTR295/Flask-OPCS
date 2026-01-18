from repository.patient_score import insert_patient_score,select_all_patient_scores
from typing import Dict,Any 

def record_patient_exam(formdata:Dict[str,Any])->bool:
    try:
        pct = round((formdata['score']/formdata['total'])*100,2)
        print(pct) 
        status = None
        if(pct>70):
            status='passes'
        elif(pct>55):
            status='conditional'
        else:
            status='failed'

        insert_patient_score(pid=formdata['pid'],qid=formdata['qid'],score=formdata['score'],total=formdata['toal'],status=status,percentage=pct)
        return True
    except Exception as e:
        print(f"Error in recording patirnt exam: {e}")
    return False

def list_passing_scores(rating:float):
    exams = [rec for rec in select_all_patient_scores() if rec[6]>=rating]
    return exams