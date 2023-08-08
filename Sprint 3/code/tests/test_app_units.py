import sys
import os

# Get the absolute path of the directory containing 'app.py'
app_dir = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.join(app_dir, '..')
sys.path.insert(0, app_path)

import pytest
from app import app
from datetime import datetime
from Models.User import User
from Models.JobPosting import JobPosting
from Models.Student import Student 

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def app_ctx(client):
    with app.app_context():
        yield

def test_signup(client): # Unit Test for SignUp
    formData = {"username": "teststudent1", "password": "teststudent1pass", "usertype": "student", "useremail": "teststudent1@me.com" }
    response = client.post('/signUp', data=formData)
    # response.status_code=200
    # response.data='user created successfully'
    assert response.status_code==200
    assert b"user created successfully" in response.data # User SignUp Successful

def test_login(client): # Unit Test for Login
    formData = {"username": "teststudent1", "password": "teststudent1pass"}
    response = client.post('/login', data=formData)
    # response.status_code=200
    # response.json['message']="success"
    assert response.status_code==200
    assert response.json['message'] == 'success' # User Login Successful

def test_postJob(client): # Unit Test for Post Job
    # Creating a test employer to post a job
    testEmployer=User('testemployer1', 'testemployer1pass', 'employer', 'testemployer1@me.com')
    formData = {"username": testEmployer.username, "password": testEmployer.password, "usertype": testEmployer.usertype, "useremail": testEmployer.useremail}
    response = client.post('/signUp', data=formData)
    # response.status_code=200
    # response.data='user created successfully'
    assert response.status_code==200
    assert b"user created successfully" in response.data # User signup successful, Test employer created successfully
    
    testEmployer=User.get_user_by_username(formData["username"])
    start='08/01/2023'
    end='08/31/2023'
    testJobPosting = JobPosting('DevOps Engineer', 'Well-versed in Kubernetes, Jenkins, and containerized applications; Requires 3+ experience', start, end, 'Vancouver, Canada', 'Full-time')
    formData={'title': testJobPosting.title, 'description': testJobPosting.description, 'startDate': start, 'endDate': end, 'location': testJobPosting.location, 'jobType': testJobPosting.jobType, 'employer_id': testEmployer.id}
    response = client.post('/postJob', data=formData)
    # response.status_code=200
    # response.data='job saved success'
    assert response.status_code==200
    assert b"job saved success" in response.data # Job posting saved successfully

def test_studentProfilePostReq(client, app_ctx): # Unit Test for Student profile creation
    testStudent=User('test','test','test','test')
    testStudent=User.get_user_by_username('teststudent1')
    formData = {
    'username': 'john_doe',
    'highestQualification': 'PhD',
    'work_experience': '5 years',
    'achivements': 'Award winner',
    'email': 'john@example.com',
    'gender': 'Male',
    'age': '1993-11-13',
    'address': '123 Main Street',
    'phone': '123-456-7890',
    'userId': testStudent.id,
    'resume':open('D:\Important_Docs\Himanshu Rathod Resume.pdf','rb')
    }

    response=client.post('/studentProfilePostReq', data=formData)
    # response.status_code=200
    # response.json['msg']="student created success"
    assert response.status_code==200
    assert response.json['msg'] == 'student created success'

def test_applyJob(client, app_ctx): # Unit Test for Apply Job
    testJob=JobPosting.get_job_by_id(1)
    testStudent=Student.get_user_by_email('john@example.com')
    formData = {"jobposting_id": testJob.id, "stud_id": testStudent.id}
    response = client.post('/applyJob', data=formData)
    assert response.status_code==200
    assert b"Job linked to student success" in response.data # Job Applied successfully ~ Student-Job realtionship established

def test_selectStudent(client, app_ctx): # Unit Test for Student Selection
    testEmployer=User.get_user_by_username('testemployer1')
    testStudent=Student.get_user_by_email('john@example.com')
    formData = {"emp_id": testEmployer.id, "stud_id": testStudent.id}
    response = client.post('/selectStudent', data=formData)
    # response.status_code=200
    # response.data='Emp Stu relationship created'
    assert response.status_code==200
    assert b"Emp Stu relationship created" in response.data # Student selected successfully ~ Employer-Student relationship established

def test_showAllUsers(client): # Unit Test for Show all users
    response = client.get('/showAllUsers')
    # response.status_code=200
    # response.json['message']="success"
    assert response.status_code==200
    assert response.json['message'] == 'success' # Users' list fetching successful

def test_deleteJob(client, app_ctx): # Unit Test for Delete Job
    testJob=JobPosting.get_job_by_id(1)
    formData = {"job_id": testJob.id}
    response = client.post('/deleteJob', data=formData)
    # response.status_code=200
    # response.data='job deleted success'
    assert response.status_code==200
    assert b"job deleted success" in response.data # Job Deleted successfully

def test_deleteUser(client, app_ctx): # Unit Test for Delete User
    testUser=User.get_user_by_username('testemployer1')
    formData = {"user_id": testUser.id}
    response = client.post('/deleteUser', data=formData)
    # response.status_code=200
    # response.data='user deleted successfully'
    assert response.status_code==200
    assert b"user deleted successfully" in response.data # User Deleted successfully

if __name__ == '__main__':
    pytest.main()