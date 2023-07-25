from flask_restful import reqparse, Resource
from Models.User import User,bcrypt
from flask import url_for

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username', type=str, required=True, help='Add the username into the system')
_user_parser.add_argument('password', type=str, required=True, help='Add the password into the system')
_user_parser.add_argument('usertype',type=str, required=False, help='Add the type of user into the system')
_user_parser.add_argument('useremail',type=str, required=False, help='Add the email of user')
class CrUser(Resource):
    def post(self):
        data = _user_parser.parse_args()
        user = User(**data)
        user.save_to_db()
        return "user created successfully"

class UserLogin(Resource):
    def post(self):
        data = _user_parser.parse_args()
        user = User.get_user_by_username(data['username'])
        if user and bcrypt.check_password_hash(user.password,data['password']):
            if user.usertype == "employer":
                return {'message' : 'success', 'name' : user.username, 'redirect_url': url_for('emp_dashboard')}
            if user.usertype == "admin":
                return {'message' : 'success', 'name' : user.username, 'redirect_url': url_for('admin_dashboard')}
            elif user.usertype == "student":
                return {'message' : 'success', 'name': user.username, 'redirect_url': url_for('student_dashboard')}
            
            return "user logged in successfully"
        else:
            return "login failed"


