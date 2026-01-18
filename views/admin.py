from __main__ import app 
from flask import redirect,Response,url_for 
from repository.admin import select_admin_join_user 

@app.route('/admin/signup/<path:address>')
def access_signup_page(address:str):
    return redirect(url_for('report_exam_list')) 

@app.route('/admin/users/list')
def generate_admin_users():
    users = select_admin_join_user()
    print(users) 
    user_list = [list[rec] for rec in users]
    print(user_list)
    content = ''' 
                <html>
                    <head>
                        <title>User List</title>
                    </head>
                    <body>
                        <h1>List Of Users</h1>
                        <p>{}
                    </body>
                </html>
        '''.format(user_list) 
    res = Response(response=content,status=200,content_type='text/html') 
    return res