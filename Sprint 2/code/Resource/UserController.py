from flask_restful import reqparse, Resource
from Models.User import User

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username', type=str, required=True, help='Add the username into the system')
_user_parser.add_argument('password', type=str, required=True, help='Add the password into the system')

class CrUser(Resource):
    def post(self):
        print("before")
        data = _user_parser.parse_args()
        print("after")
        print(data)
        user = User(**data)
        user.save_to_db()
        print("user created")
        return "user created successfully"