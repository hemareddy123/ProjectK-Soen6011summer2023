from flask_restful import reqparse, Resource
from Models.Employer import Employer

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('first_name', type=str, required=True, help='Add the employee first name')
_user_parser.add_argument('last_name', type=str, required=True, help='Add the employee last name')
_user_parser.add_argument('email', type=str, required=True, help='Add the email of employee')
_user_parser.add_argument('organization', type=str, required=True, help='Add the organization of employee')
_user_parser.add_argument('phone', type=str, required=True, help='Add the phone number of employee')
_user_parser.add_argument('designation', type=str, required=True, help='Add the designation of employee')


class signupEmp(Resource):

    def post(self):
        data = _user_parser.parse_args()
        empUser = Employer(**data)
        empUser.save_to_db()
        print("Employer Profile Saved")
        return "Employer Profile Saved"
