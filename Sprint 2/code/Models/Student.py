from db import db
from datetime import datetime

class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, nullable=True)
    highestQualification = db.Column(db.Integer,nullable=True)
    work_experience = db.Column(db.Integer, nullable=True)
    achivements = db.Column(db.String(150), nullable=True)
    email = db.Column(db.String(15),nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    age = db.Column(db.DateTime,nullable=True)
    address = db.Column(db.String(50), nullable=True)
    phone = db.Column(db.String(15), nullable=True)
    

    def __init(self,username,highestQualification,work_experience,achievements,email,gender,age,address,phone):
        self.username = username
        self.highestQualification = highestQualification
        self.work_experience = work_experience
        self.achievements = achievements
        self.email = email
        self.gender = gender
        self.age = age
        self.address = address
        self.phone = phone

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_students(cls):
        return cls.query.all()

    @classmethod
    def get_user_by_email(cls, email_):
        return cls.query.filter_by(email=email_).first()
    
    @classmethod
    def get_user_by_id(cls, id_):
        return cls.query.filter_by(id=id_).first()