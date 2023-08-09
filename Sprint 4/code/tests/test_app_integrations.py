import sys
import os
import json

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

def test_signup_login_integration(client): # Integration Test for Sign Up and Login
    signupFormData = {"username": "teststudent1","password": "teststudent1pass","usertype": "student","useremail": "teststudent1@me.com"}
    signupResponse = client.post('/signUp', data=json.dumps(signupFormData), content_type='application/json')
    assert signupResponse.status_code == 200
    assert b"user created successfully" in signupResponse.data  # User SignUp Successful

    loginFormData = {"username": "teststudent1", "password": "teststudent1pass"}
    loginResponse = client.post('/login', data=json.dumps(loginFormData), content_type='application/json')
    assert loginResponse.status_code==200
    assert loginResponse.json['message'] == 'success' # User Login Successful

    if(signupResponse.status_code==200 and loginResponse.status_code==200):
        print("Sign up and Login integration successful") # Sign up and Login integration successful

def test_postJob__studentProfileCreatuon_applyJob_integartion(client): # Integration Test for Post Job, Student Profile Creation, Apply Job
    # Creating a test employer to post a job
    testEmployer=User('testemployer1', 'testemployer1pass', 'employer', 'testemployer1@me.com')
    signupFormData = {"username": testEmployer.username, "password": testEmployer.password, "usertype": testEmployer.usertype, "useremail": testEmployer.useremail}
    signupResponse = client.post('/signUp', data=json.dumps(signupFormData), content_type='application/json')
    assert signupResponse.status_code==200
    assert b"user created successfully" in signupResponse.data # User signup successful, Test employer created successfully

    # Creating a test student to create profile and apply job
    testStudent=User('test','test','test','test')
    testStudent=User.get_user_by_username('teststudent1')
    profileCreationformData = {
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
    'resume': open('./Rahul Sharam_resume.pdf', 'rb')
    }
    profileCreationResponse=client.post('/studentProfilePostReq', data=profileCreationformData)
    assert profileCreationResponse.status_code==200
    assert profileCreationResponse.json['msg'] == 'student created success'
    
    # Posting a job for student to apply
    testEmployer=User.get_user_by_username(formData["signupFormData"])
    start='08/01/2023'
    end='08/31/2023'
    testJobPosting = JobPosting('DevOps Engineer', 'Well-versed in Kubernetes, Jenkins, and containerized applications; Requires 3+ experience', start, end, 'Vancouver, Canada', 'Full-time')
    postJobFormData={'title': testJobPosting.title, 'description': testJobPosting.description, 'startDate': start, 'endDate': end, 'location': testJobPosting.location, 'jobType': testJobPosting.jobType, 'employer_id': testEmployer.id}
    postJobResponse = client.post('/postJob', data=json.dumps(postJobFormData), content_type='application/json')
    assert postJobResponse.status_code==200
    assert b"job saved success" in response.data # Job posting saved successfully

    testJob=JobPosting.get_job_by_id(1)
    testStudent=Student.get_user_by_email('john@example.com')
    applyJobFormData = {"jobposting_id": testJob.id, "stud_id": testStudent.id}
    applyJobResponse = client.post('/applyJob', data=json.dumps(applyJobFormData), content_type='application/json')
    assert applyJobResponse.status_code==200
    assert b"Job linked to student success" in response.data # Job Applied successfully

    if(signupResponse.status_code==200 and profileCreationResponse.status_code==200 and postJobResponse.status_code==200 and applyJobResponse==200):
        print("Post Job, Student Profile Creation, and Apply Job integration successful")
    
if __name__ == '__main__':
    pytest.main()