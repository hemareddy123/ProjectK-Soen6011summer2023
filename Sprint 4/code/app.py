from flask import Flask, render_template, request, Response, redirect, url_for
from flask_restful import Api
from datetime import datetime
from socket_event import socketio

from db import db
from Resource.EmpStudentController import CrEmpStud
from Models.User import User
from Models.JobPosting import JobPosting
from Models.Student import Student
from Models.Chat import Chat

from Resource.UserController import CrUser,UserLogin, DlUser
from Resource.JobPostController import CrJobPosting , DlJobPosting
from Resource.StudentController import CrStudent , CrStudJob
from Resource.AdminController import ShowAllUsers
from Resource.ChatController import CrChat
from datetime import datetime

#Root file for running the application
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
socketio.init_app(app)

# Dropping the all previous table and creating new one, on every restart of application
@app.before_first_request
def create_tables():
    #db.drop_all()
    db.create_all()

api = Api(app)

# Home Route
@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

#Employee Dashboard Route
@app.route('/emp_dashboard')
def emp_dashboard():
    id = request.args.get('id')
    emp = User.get_user_by_id(id)
    jobs = JobPosting.get_all_jobs()
    students = emp.applied_students
    selectedStudents = emp.selected_students
    return render_template('empDashboard.html',
                            empId=emp.id,
                            username=emp.username,
                            email=emp.useremail,
                            jobs=jobs,
                            students=students,
                            selectedStudents=selectedStudents)

# Admin Dashboard Route
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
 
# Student Profile Form Route
@app.route('/studentProfileForm')
def studentProfileForm():
    userId = request.args.get('id')
    user = User.get_user_by_id(userId)

    student = user.user_students
    if len(student) == 1:
        return redirect(url_for('student_dashboard', userId=userId, id=student[0].id))
    else:
        return render_template('studentProfileForm.html',user=user)

# Student Dashboard Route
@app.route('/studentDashBoard')
def student_dashboard():
    studentId = request.args.get('id')
    user = request.args.get('userId')
    student = Student.get_user_by_id(studentId)
    user = User.get_user_by_id(user)

    user_student = user.user_students
    if len(user_student) == 0:
        user.user_students.append(student)
        db.session.commit()

    jobs = JobPosting.get_all_jobs()
    selectedJobs = student.selectedJobs
    return render_template('studentDashboard.html',student=student,jobs=jobs,user=user,selectedJobs=selectedJobs)

# Student Profile Route
@app.route('/studentProfile')
def student_profile():
    studentId = request.args.get('id')
    student = Student.get_user_by_id(studentId)
    return render_template('studentProfile.html',student=student)

# Download the resume for the student Profile
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

# chat route for employer
@app.route('/chat')
def chat():
    
    studId = request.args.get('studid')
    student = Student.get_user_by_id(studId)

    empId = request.args.get('empid')
    initater = request.args.get('initater')
    chats = Chat.get_chat_by_empId_studId(empId,studId)

    employer = User.get_user_by_id(empId)
    

    return render_template('chat.html',stuId=studId,empId=empId,initater=initater,chats=chats,employer=employer,student=student)

# student chat route
@app.route('/studentChat')
def studentChat():
    studId = request.args.get('studid')
    initater = 'student'
    job_id = request.args.get('jobid')

    student = Student.get_user_by_id(studId)

    job = JobPosting.get_job_by_id(job_id)
    employer = job.createdByEmployer[0]
    empId = employer.id


    chats = Chat.get_chat_by_empId_studId(empId,studId)
    return render_template('chat.html',stuId=studId,empId=empId,initater=initater,chats=chats,employer=employer,student=student)

# Filtering the age to proper format and calculating his current age
@app.template_filter('age_format')
def age_format(date_of_birth):
    age = calculate_age(date_of_birth)
    return f"{age} years"

def calculate_age(date_of_birth):
    today = datetime.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    return age


# core api's that are required for supporting tasks.

api.add_resource(UserLogin,"/login")
api.add_resource(CrUser,"/signUp")
api.add_resource(CrJobPosting,"/postJob")
api.add_resource(CrStudent,"/studentProfilePostReq")
api.add_resource(CrEmpStud,"/selectStudent")
api.add_resource(ShowAllUsers,"/showAllUsers")
api.add_resource(CrStudJob,"/applyJob")
api.add_resource(DlJobPosting,"/deleteJob")
api.add_resource(DlUser,"/deleteUser")
api.add_resource(CrChat,'/createChat')

if __name__ == '__main__':
    # app.run(debug=True)
    socketio.run(app,debug=True)

