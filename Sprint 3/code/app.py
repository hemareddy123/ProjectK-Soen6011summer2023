from io import BytesIO
from flask import Flask, render_template, request, Response, redirect, url_for
from flask_restful import Api, Resource
from db import db
from Resource.EmpStudentController import CrEmpStud
from Models.User import User
from Models.JobPosting import JobPosting
from Models.Student import Student

from Resource.UserController import CrUser,UserLogin
from Resource.JobPostController import CrJobPosting
from Resource.StudentController import CrStudent
from Resource.AdminController import ShowAllUsers


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

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
    username = request.args.get('username')
    emp = User.get_user_by_username(username)
    jobs = JobPosting.get_all_jobs()
    students = Student.get_all_students()
    selectedStudents = emp.selected_students
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
    user=User.get_user_by_username(username)
    users = User.get_all_users()
    return render_template('adminDashboard.html',
                            username=username,
                            email=user.useremail,
                            users=users)
 
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
    print(len)
    if len(user_student) == 0:
        user.user_students.append(student)
        db.session.commit()

    jobs = JobPosting.get_all_jobs()
    return render_template('studentDashboard.html',student=student,jobs=jobs,user=user)

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

def student_dashboard():
    username = request.args.get()


api.add_resource(UserLogin,"/login")
api.add_resource(CrUser,"/signUp")
api.add_resource(CrJobPosting,"/postJob")
api.add_resource(CrStudent,"/studentProfilePostReq")
api.add_resource(CrEmpStud,"/selectStudent")
api.add_resource(ShowAllUsers,"/showAllUsers")

if __name__ == '__main__':
    app.run(debug=True)

