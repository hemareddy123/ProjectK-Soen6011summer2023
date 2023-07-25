from flask_restful import reqparse, Resource
from Models.User import User
from Models.Student import Student
from db import db

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('emp_id', type=int, required=True, help='Add the title of job into the system')
_user_parser.add_argument('stud_id', type=int, required=True, help='Add the description of job into the system')
class CrEmpStud(Resource):
    def post(self):
        data = _user_parser.parse_args()
        employer = User.get_user_by_id(data['emp_id'])
        student = Student.get_user_by_id(data['stud_id'])

        employer.selected_students.append(student)
        db.session.commit()
        return "Emp Stu relationship created"


