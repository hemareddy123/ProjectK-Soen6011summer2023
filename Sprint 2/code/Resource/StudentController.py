from Models.Student import Student
from flask_restful import reqparse, Resource
from flask import url_for

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('first_name', type=str, required=True, help='Add the first_name into the system')
_user_parser.add_argument('last_name', type=str, required=False, help='Add the last_name into the system')
_user_parser.add_argument('work_experience', type=int, required=False, help='Add the work_experience into the system')
_user_parser.add_argument('skills', type=str, required=False, help='Add the skills into the system')
_user_parser.add_argument('salary', type=str, required=False, help='Add the salary into the system')
_user_parser.add_argument('phone', type=str, required=False, help='Add the phone number into the system')
class CrStudent(Resource):
    def post(self):
        data = _user_parser.parse_args()
        student = Student(**data)
        student.save_to_db()
        return "student profile created"


