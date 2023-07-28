from db import db
from flask_bcrypt import Bcrypt
import json
from sqlalchemy import or_

bcrypt = Bcrypt()

# emp_stu = db.Table('emp_stu',
#     db.Column('emp_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
#     db.Column('stud_id', db.Integer, db.ForeignKey('student.id'), primary_key=True)
# )
user_stu = db.Table('user_stu',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('stud_id', db.Integer, db.ForeignKey('student.id'), primary_key=True)
)
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    usertype = db.Column(db.String(10), nullable=False)
    useremail = db.Column(db.String(20), nullable=False)


    #selected_students = db.relationship('Student',secondary='emp_stu')
    user_students = db.relationship('Student',secondary = 'user_stu')

    def __init__(self, username, password,usertype,useremail):
    
        self.username = username.lower()
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.usertype = usertype.lower()
        self.useremail = useremail

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @classmethod
    def get_user_by_username(cls, username_):
        return cls.query.filter_by(username=username_).first()
    
    @classmethod
    def get_user_by_id(cls, id_):
        return cls.query.filter_by(id=id_).first()
    
    @classmethod
    def get_all_users(cls):
        users=cls.query.filter(or_(cls.usertype=="employer", cls.usertype=="student")).all()
        return users
