from flask_restful import reqparse, Resource
from flask import url_for
from Models.JobPosting import JobPosting
from Models.User import User

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('title', type=str, required=True, help='Add the title of job into the system')
_user_parser.add_argument('description', type=str, required=True, help='Add the description of job into the system')
_user_parser.add_argument('startDate', type=str, required=True, help='Add the startdate of job into the system')
_user_parser.add_argument('endDate', type=str, required=True, help='Add the enddate of job into the system')
_user_parser.add_argument('location', type=str, required=True, help='Add the location of job into the system')
_user_parser.add_argument('jobType', type=str, required=True, help='Add the jobtype of that job into the system')
_user_parser.add_argument('employer_id', type=int, required=True, help='Add the employer id of that job into the system')

class CrJobPosting(Resource):
    def post(self):
        data = _user_parser.parse_args()
        emp_user = User.get_user_by_id(data['employer_id'])
        data.pop('employer_id')
        job = JobPosting(**data)

        job.createdByEmployer.append(emp_user)
        
        job.save_to_db()
        return "job saved success"
    
