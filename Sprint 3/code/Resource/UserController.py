from flask_restful import reqparse, Resource
from Models.User import User,bcrypt
from flask import url_for
from db import db

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
                return {'message' : 'success', 'userId' : user.id,  'type' : 'employer', 'redirect_url': url_for('emp_dashboard')}
            elif user.usertype == "admin":
                return {'message' : 'success', 'name' : user.username, 'redirect_url': url_for('admin_dashboard'), 'type' : user.usertype}
            elif user.usertype == "student":
                return {'message' : 'success','type':'student' ,'userId' : user.id,'redirect_url': url_for('studentProfileForm'), 'type' : user.usertype}
            
            return "user logged in successfully"
        else:
            return "login failed"

_user_parser1 = reqparse.RequestParser()   
_user_parser1.add_argument('user_id', type=int, required=True, help='Delete user id ')   
class DlUser(Resource):
    def post(self):
        data = _user_parser1.parse_args()
        user = User.get_user_by_id(data['user_id'])
        db.session.delete(user)
        db.session.commit()
        return "user deleted successfully"

