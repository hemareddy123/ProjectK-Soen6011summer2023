from flask_restful import reqparse, Resource
from Models.Chat import Chat

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('empId', type=int, required=True, help='Add the employer id linked into the system')
_user_parser.add_argument('studId', type=int, required=True, help='Add the student id linked into the system')
_user_parser.add_argument('initater', type=str, required=True, help='Add the initator heading into the system')
_user_parser.add_argument('text',type=str, required=True, help='Text of the job')
class CrChat(Resource):
    def post(self):
        data = _user_parser.parse_args()
        print('here is the value of initator' + str(data['initater']))
        chat = Chat(**data)
        chat.save_to_db()
        
        return "chat created successfully"


