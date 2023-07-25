from flask_restful import reqparse, Resource
from Models.User import User,bcrypt
from flask import url_for
import json

class ShowAllUsers(Resource):
    def get(self):
        users = json.dumps(User.get_all_users())
        return users

