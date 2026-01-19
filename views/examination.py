from __main__ import app  
from flask import request,render_template,redirect,url_for,make_response
from services.utility import list_cid,list_pid,list_qid
from repository.question_details import insert_question_detail
from services.patient_monitoring import record_patient_exam,list_patient_scores
from services.exam_management import add_exam_item,list_exam_details 

@app.route('/exam/assign',methods=['GET','POST'])
def assign_exam():
    if request.method=='GET':
        cids = list_cid()
        pids = list_pid()
        response = make_response(render_template('exam/assign_exam_form.html',cids=cids,pids=pids),200) 
        response.set_cookie('exam_token',str(uuid4())) 
        return response , 200 
    else:
        id = int(request.form['id']) 
        cid = request.form['cid']
        pid = int(request.form['pid'])
        exam_date = request.form['exam_date']
        duration = int(request.form['duration'])
        result = insert_question_detail(id=id,cid=cid,pid=pid,exam_date=exam_date,duration=duration)
        if result:
            task_token = request.cookies.get('exam_token')
            task = "exam assignment (task id: {})".format(task_token)
            return redirect(url_for('redirect_success_exam',message=task))
        
@app.route('/exam/success',methods=['GET'])
def redirect_success_exam():
    message = request.args['message']
    return render_template('exam/redirect_success_view.html',message=message) 

@app.route('/exam/task/error',methods=['GET'])
def redirect_error_exam():
    return render_template('error/redirect_exam_error.html')

@app.route('/exam/score',methods=['GET','POST'])
def record_score():
    if request.method=='GET':
        pids = list_pid()
        qids = list_qid()
        return render_template('exam/add_patient_score_form.html',pids=pids,qids=qids),200 
    else:
        params = dict()
        params['pid'] = int(request.form['pid'])
        params['qid'] = int(request.form['qid'])
        params['score'] = float(request.form['score'])
        params['total'] = float(request.form['total'])
        result = record_patient_exam(params)
        if result:
            task = 'recording exam score'
            response = make_response()
            headers = dict()
            headers['Location'] = url_for('redirect_success_exam',message=task) 
            response.headers = headers 
            return response , 302 
        else:
            return redirect('/exam/task/error') 

@app.route('/exam/item/add',methods=['GET','POST'])
def add_exam_item():
    if request.method=='GET':
        qids = list_qid()
        return render_template('exam/add_exam_form.html',qids=qids)
    else:
        qid = int(request.form['qid'])
        qtype = int(request.form['question_type'])
        result = False 
        if qtype==1:
            question = request.form['mchoiceq'] 
            print(question) 
            choices = dict()
            choices['a'] = request.form['choice1'] 
            choices['b'] = request.form['choice2'] 
            choices['c'] = request.form['choice3'] 
            choices['d'] = request.form['choice4'] 
            print(choices) 
            answers = request.form.getlist('answers') 
            print(answers) 
            result = add_exam_items(qid=qid,qtype=qtype,question=question,params=choices,ans_essay=None,answers=answers)
        elif qtype==2:
            question = request.form['essayq'] 
            answer = request.form['ans_essay'] 
            result = add_exam_items(qid=qid,qtype=qtype,question=question,ans_essay=answer)
        if result:
            task = 'adding items to exam {}'.format(qid)
            url = "/exam/item/add"
            return redirect(url_for('redirect_success_exam',message=task))
        else:
            return redirect('/exam/task/error') 

@app.route('/exam/details/list')
def report_exam_list():
    exams = list_exam_details()
    response = make_response(render_template('exam/list_exams.html',exams=exams),200) 
    headers = dict()    
    headers['Content-Type']='application/vnd.ms-excel'
    headers['Content-Disposition']='attachment; filename=questions.xlsx'
    response.headers = headers 
    return response 

@app.route('/exam/passers/list/<float:rate>/<uuid:docId>')
def report_exam_passers(rate:float,docId:uuid=None):
    exams = list_patient_scores(rate)
    response = make_response(render_template('exam/list_exam_passers.html',exams=exams,docId=docId),200) 
    return response 

    