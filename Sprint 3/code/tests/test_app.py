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

def test_signup(client): # Unit Test for SignUp
    formData = {"username": "teststudent1", "password": "teststudent1pass", "usertype": "student", "useremail": "teststudent1@me.com"}
    response = client.post('/signUp', data=formData)
    assert response.status_code==200
    assert b"user created successfully" in response.data # User SignUp Successful

def test_login(client): # Unit Test for Login
    formData = {"username": "teststudent1", "password": "teststudent1pass"}
    response = client.post('/login', data=formData)
    assert response.status_code==200
    assert response.json['message'] == 'success' # User Login Successful

def test_postJob(client): # Unit Test for Post Job
    # Creating a test employer to post a job
    testEmployer=User('testemployer1', 'testemployer1pass', 'employer', 'testemployer1@me.com')
    formData = {"username": testEmployer.username, "password": testEmployer.password, "usertype": testEmployer.usertype, "useremail": testEmployer.useremail}
    response = client.post('/signUp', data=formData)
    assert response.status_code==200
    assert b"user created successfully" in response.data # User signup successful, Test employer created successfully
    
    testEmployer=User.get_user_by_username(formData["username"])
    start='08/01/2023'
    end='08/31/2023'
    testJobPosting = JobPosting('DevOps Engineer', 'Well-versed in Kubernetes, Jenkins, and containerized applications; Requires 3+ experience', start, end, 'Vancouver, Canada', 'Full-time')
    formData={'title': testJobPosting.title, 'description': testJobPosting.description, 'startDate': start, 'endDate': end, 'location': testJobPosting.location, 'jobType': testJobPosting.jobType, 'employer_id': testEmployer.id}
    response = client.post('/postJob', data=formData)
    assert response.status_code==200
    assert b"job saved success" in response.data # Job posting saved successfully

def test_selectStudent(client): # Unit Test for Student Selection
    formData = {"username": "teststudent1", "password": "teststudent1pass"}
    response = client.post('/login', data=formData)
    assert response.status_code==200
    assert response.json['message'] == 'success' # User Login Successful

# @pytest.mark.usefixtures("client")
# def test_studentProfilePostReq(client):
#     testStudent=User.get_user_by_username('teststudent1')
#     formData = {
#     'username': 'john_doe',
#     'highestQualification': 'PhD',
#     'work_experience': '5 years',
#     'achivements': 'Award winner',
#     'email': 'john@example.com',
#     'gender': 'Male',
#     'age': '1993-11-13',
#     'address': '123 Main Street',
#     'phone': '123-456-7890',
#     'userId': testStudent.id
#     }

#     files={
#         'resume':open('D:\Important_Docs\Himanshu Rathod Resume','rb')
#     }

#     response=client.post('/studentProfilePostReq', data=formData, files=files)
#     assert response.status_code==200
#     assert response.json['msg'] == 'student created success'

if __name__ == '__main__':
    pytest.main()
