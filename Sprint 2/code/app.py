from flask import Flask, render_template, request
from flask_restful import Api, Resource
from db import db
from Resource.EmpStudentController import CrEmpStud
from Models.User import User
from Models.JobPosting import JobPosting
from Models.Student import Student

from Resource.UserController import CrUser,UserLogin
from Resource.JobPostController import CrJobPosting
from Resource.StudentController import CrStudent
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
    students = Student.get_all_students()
    selectedStudents = emp.selected_students
    print("selected Students ")
    print(selectedStudents)
    return render_template('empDashboard.html',empId=emp.id,username=emp.username,email=emp.useremail,jobs=jobs,students=students)

@app.route('/student_dashboard')
def student_dashboard():
    return render_template('studentDashboard.html')


def student_dashboard():
    username = request.args.get()

api.add_resource(UserLogin,"/login")
api.add_resource(CrUser,"/signUp")
api.add_resource(CrJobPosting,"/postJob")
api.add_resource(CrStudent,"/studentProfile")
api.add_resource(CrEmpStud,"/selectStudent")

if __name__ == '__main__':
    app.run()
