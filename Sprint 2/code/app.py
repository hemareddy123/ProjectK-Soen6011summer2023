from flask import Flask, render_template, request
from flask_restful import Api, Resource
from db import db
from Models.User import User
from Models.JobPosting import JobPosting

from Resource.UserController import CrUser,UserLogin
from Resource.JobPostController import CrJobPosting

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    #db.drop_all()
    db.create_all()

api = Api(app)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/emp_dashboard')
def emp_dashboard():
    username = request.args.get('username')
    emp = User.get_user_by_username(username)
    jobs = JobPosting.get_all_jobs()

    return render_template('empDashboard.html',username=emp.username,email=emp.useremail,jobs=jobs)

api.add_resource(UserLogin,"/login")
api.add_resource(CrUser,"/signUp")
api.add_resource(CrJobPosting,"/postJob")

if __name__ == '__main__':
    app.run()
