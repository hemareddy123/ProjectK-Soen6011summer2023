from db import db

class Candidate(db.Model):
    __tablename__ = 'candidate'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    qualification = db.Column(db.String(50), nullable=False)
    skills = db.Column(db.String(15), nullable=False)
    work_experience = db.Column(db.String(15), nullable=False)
    education = db.Column(db.String(15), nullable=False)
    expected_salary = db.Column(db.Integer)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def get_user_by_username(self):
        return
