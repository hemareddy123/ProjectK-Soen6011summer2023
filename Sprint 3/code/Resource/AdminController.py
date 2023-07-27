from flask_restful import reqparse, Resource
from Models.User import User,bcrypt
from flask import url_for, render_template
import json

class ShowAllUsers(Resource):
    def get(self):
        users={}
        usersList=User.get_all_users()
        for user in usersList:
            users.update({'username':user.username, 'useremail':user.useremail, 'usertype':user.usertype})
        return {'message' : 'success', 'users': users} 