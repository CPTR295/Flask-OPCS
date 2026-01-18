from flask import Flask 
from convertor.date_convertor import DateConvertor

app = Flask(__name__,template_folder='pages') 
app.config.from_pyfile('myconfig.py') 

app.url_map.converters['date'] = DateConvertor

@app.route('/')
def index():
    return "This is an online personal counseling system(OPCS)!"

import views.index
import views.certificates
import views.signup
import views.login
import views.admin
import views.profile
import views.examination
import views.reports
from views.contract import ContractView,DeleteContractByPIDView,ListUnpaidContractView

app.add_url_rule('/certiticate/terminate/<string:counselor>/<date:effecive_date>/<string:patient>','show_honor_dissmisal',views.certificates.show_honor_dissmisal)
app.add_url_rule('/contract/patient/add/form',view_func=ContractView.as_view('contract-view'))
app.add_url_rule('/contract/patient/delete',view_func=DeleteContractByPIDView.as_view('delete-contract-view'))
app.add_url_rule('/contract/patient/unpaid',view_func=ListUnpaidContractView.as_view('list-unpaid-view'))

if __name__ == '__main__':
    app.run(debug=True)

