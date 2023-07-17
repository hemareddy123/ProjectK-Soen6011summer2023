from flask import Flask, render_template
from flask_restful import Api, Resource
from db import db

from Resource.UserController import CrUser,UserLogin;

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    #db.drop_all()
    db.create_all()

api = Api(app)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

api.add_resource(UserLogin,"/login")
api.add_resource(CrUser,"/signUp")


#api.add_resource(signupEmp,"/employerProfile")
api.add_resource(CrUser,"/signUp")

if __name__ == '__main__':
    app.run()
