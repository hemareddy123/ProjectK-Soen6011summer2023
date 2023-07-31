from flask_restful import reqparse, Resource
from Models.JobPosting import JobPosting
from Models.User import User
from Models.Student import Student
from db import db

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('title', type=str, required=True, help='Add the title of job into the system')
_user_parser.add_argument('description', type=str, required=True, help='Add the description of job into the system')
_user_parser.add_argument('startDate', type=str, required=True, help='Add the startdate of job into the system')
_user_parser.add_argument('endDate', type=str, required=True, help='Add the enddate of job into the system')
_user_parser.add_argument('location', type=str, required=True, help='Add the location of job into the system')
_user_parser.add_argument('jobType', type=str, required=True, help='Add the jobtype of that job into the system')
_user_parser.add_argument('employer_id', type=int, required=True, help='Add the employer id of that job into the system')

class CrJobPosting(Resource):
    def post(self):
        data = _user_parser.parse_args()
        emp_user = User.get_user_by_id(data['employer_id'])
        data.pop('employer_id')
        job = JobPosting(**data)

        job.createdByEmployer.append(emp_user)
        
        job.save_to_db()
        return "job saved success"
    

_user_parser1 = reqparse.RequestParser()
_user_parser1.add_argument('job_id', type=int, required=True, help='Remove job from the system')
class DlJobPosting(Resource):
    def post(self):
        data = _user_parser1.parse_args()
        jobToBeDeleted = JobPosting.get_job_by_id(data['job_id'])
        
        # Remove that job from the student applied section
        students = Student.get_all_students();
        for student in students:
            jobs = student.selectedJobs
            for job in jobs:
                if jobToBeDeleted == job:
                    jobs.remove(jobToBeDeleted)
                    break
        
        # Remove the student from the employer applied student table
        employer = jobToBeDeleted.createdByEmployer
        if len(employer) > 0:
            appliedStudents = employer[0].applied_students
            appliedStudents.clear()

        db.session.delete(jobToBeDeleted)
        db.session.commit()
        
        return 'job deleted success'
        



        
    
