from Models.Student import Student
from flask_restful import reqparse, Resource
from flask import url_for
from werkzeug.datastructures import FileStorage

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

        #print(resume_data)
        #return {'success': 'student generated'}

        student = Student(resume=resume_data, **data)
        student.save_to_db()
        return {'studentId': student.id, 'msg': 'student created success'}



