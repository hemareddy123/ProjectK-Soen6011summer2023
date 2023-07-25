from db import db

class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    work_experience = db.Column(db.Integer, nullable=True)
    skills = db.Column(db.String(150), nullable=True)
    salary = db.Column(db.String(15), nullable=True)
    phone = db.Column(db.String(15), nullable=True)

    def __init__(self,first_name,last_name,work_experience,skills,salary,phone):
        self.first_name = first_name
        self.last_name = last_name
        self.work_experience = work_experience
        self.skills = skills
        self.salary = salary
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