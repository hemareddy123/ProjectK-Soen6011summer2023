from Models.Student import Student
from Models.JobPosting import JobPosting
from flask_restful import reqparse, Resource
from werkzeug.datastructures import FileStorage
from db import db

_user_parser = reqparse.RequestParser()

_user_parser.add_argument('username', type=str, required=False, help='Add the username into the system',location="form")
_user_parser.add_argument('highestQualification', type=str, required=False, help='Add the highestQualification into the system',location="form")
_user_parser.add_argument('work_experience', type=str, required=False, help='Add the work_experience into the system',location="form")
_user_parser.add_argument('achivements', type=str, required=False, help='Add the achivements into the system',location="form")
_user_parser.add_argument('email', type=str, required=False, help='Add the email into the system',location="form")
_user_parser.add_argument('gender', type=str, required=False, help='Add the gender into the system',location="form")
_user_parser.add_argument('age', type=str, required=False, help='Add the age into the system',location="form")
_user_parser.add_argument('address', type=str, required=False, help='Add the address into the system',location="form")
_user_parser.add_argument('phone', type=str, required=False, help='Add the phone number into the system',location="form")
_user_parser.add_argument('resume', type=FileStorage, location='files', required=False, help='Upload resume (PDF)')

class CrStudent(Resource):
    def post(self):
        data = _user_parser.parse_args()
        
        resume_file = data['resume']
        resume_data = None
        if resume_file:
            resume_data = resume_file.read()
        
        data.pop('resume',None)

        # print(resume_data)
        # return {'success': 'student generated'}

        student = Student(resume=resume_data, **data)
        student.save_to_db()
        return {'studentId': student.id, 'msg': 'student created success'}
    

# created relationship b/w student and a job

_user_parser1 = reqparse.RequestParser()
_user_parser1.add_argument('stud_id', type=int, required=False, help='Add the student-id into the system')
_user_parser1.add_argument('jobposting_id', type=int, required=False, help='Add the jobposting-id into the system')

class CrStudJob(Resource):
    def post(self):
        data = _user_parser1.parse_args()
        stu_id = data['stud_id']
        job_id = data['jobposting_id']

        student = Student.get_user_by_id(stu_id)
        job = JobPosting.get_job_by_id(job_id)
        
        #hoping to create a relationship b/w applied students and posted employer
        employer = job.createdByEmployer[0]
        employer.applied_students.append(student)

        student.selectedJobs.append(job)
        student.status = 'Applied'
        db.session.commit()

        return "Job linked to student success"












