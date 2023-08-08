from flask import Flask, render_template, request, Response, redirect, url_for
from flask_restful import Api, Resource
from socket_events import socketio

from db import db
from Resource.EmpStudentController import CrEmpStud
from Models.User import User
from Models.JobPosting import JobPosting
from Models.Student import Student

from Resource.UserController import CrUser,UserLogin, DlUser
from Resource.JobPostController import CrJobPosting , DlJobPosting
from Resource.StudentController import CrStudent , CrStudJob
from Resource.AdminController import ShowAllUsers
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
socketio.init_app(app)

@app.before_first_request
def create_tables():
    db.drop_all()
    db.create_all()

api = Api(app)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/emp_dashboard')
def emp_dashboard():
    id = request.args.get('id')
    emp = User.get_user_by_id(id)
    jobs = JobPosting.get_all_jobs()
    students = emp.applied_students
    selectedStudents = emp.selected_students
    # print('below is the type')
    # print(type(students))
    #selectedStudents = emp.selected_students
    return render_template('empDashboard.html',
                            empId=emp.id,
                            username=emp.username,
                            email=emp.useremail,
                            jobs=jobs,
                            students=students,
                            selectedStudents=selectedStudents)

@app.route('/admin_dashboard')
def admin_dashboard():
    username = request.args.get('username')
    admin=User.get_user_by_username(username)
    
    users = User.get_all_users()
    students = Student.get_all_students()
    
    jobs = JobPosting.get_all_jobs()
    return render_template('adminDashboard.html',
                            username=username,
                            email=admin.useremail,
                            users=users,
                            jobs=jobs)
 
@app.route('/studentProfileForm')
def studentProfileForm():
    userId = request.args.get('id')
    user = User.get_user_by_id(userId)

    student = user.user_students
    if len(student) == 1:
        return redirect(url_for('student_dashboard', userId=userId, id=student[0].id))
    else:
        return render_template('studentProfileForm.html',user=user)

@app.route('/studentDashBoard')
def student_dashboard():
    studentId = request.args.get('id')
    user = request.args.get('userId')
    student = Student.get_user_by_id(studentId)
    user = User.get_user_by_id(user)

    # Hack not to be used for proper architecture
    user_student = user.user_students
    if len(user_student) == 0:
        user.user_students.append(student)
        db.session.commit()

    jobs = JobPosting.get_all_jobs()
    selectedJobs = student.selectedJobs
    return render_template('studentDashboard.html',student=student,jobs=jobs,user=user,selectedJobs=selectedJobs)

@app.route('/studentProfile')
def student_profile():
    studentId = request.args.get('id')
    student = Student.get_user_by_id(studentId)
    return render_template('studentProfile.html',student=student)

@app.route('/download_resume')
def download_resume():
    studentId = request.args.get('id')
    print('student is '+ studentId)

    student = Student.get_user_by_id(studentId)

    resume_data = student.resume
    # You can set the appropriate filename for the downloaded resume
    resume_filename = student.username + "_resume.pdf"

    response = Response(resume_data, content_type='application/pdf')
    response.headers['Content-Disposition'] = f'attachment; filename={resume_filename}'

    return response

@app.route('/chat')
def chat():
    return render_template('chat.html')

def student_dashboard():
    username = request.args.get()

@app.template_filter('age_format')
def age_format(date_of_birth):
    age = calculate_age(date_of_birth)
    return f"{age} years"

def calculate_age(date_of_birth):
    today = datetime.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    return age


api.add_resource(UserLogin,"/login")
api.add_resource(CrUser,"/signUp")
api.add_resource(CrJobPosting,"/postJob")
api.add_resource(CrStudent,"/studentProfilePostReq")
api.add_resource(CrEmpStud,"/selectStudent")
api.add_resource(ShowAllUsers,"/showAllUsers")
api.add_resource(CrStudJob,"/applyJob")
api.add_resource(DlJobPosting,"/deleteJob")
api.add_resource(DlUser,"/deleteUser")

if __name__ == '__main__':
    app.run(debug=True)

