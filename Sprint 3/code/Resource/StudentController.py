from Models.Student import Student
from flask_restful import reqparse, Resource
from flask import url_for

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username', type=str, required=False, help='Add the username into the system')
_user_parser.add_argument('highestQualification', type=str, required=False, help='Add the highestQualification into the system')
_user_parser.add_argument('work_experience', type=str, required=False, help='Add the work_experience into the system')
_user_parser.add_argument('achivements', type=str, required=False, help='Add the achivements into the system')
_user_parser.add_argument('email', type=str, required=False, help='Add the email into the system')
_user_parser.add_argument('gender', type=str, required=False, help='Add the gender into the system')
_user_parser.add_argument('age', type=str, required=False, help='Add the age into the system')
_user_parser.add_argument('address', type=str, required=False, help='Add the address into the system')
_user_parser.add_argument('phone', type=str, required=False, help='Add the phone number into the system')

class CrStudent(Resource):
    def post(self):
        data = _user_parser.parse_args()
        student = Student(**data)
        student.save_to_db()
        return {'studentId': student.id, 'msg': 'student created success'}


