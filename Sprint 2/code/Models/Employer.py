from db import db

class Employer(db.Model):
    __tablename__ = 'employer'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    organization = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    designation = db.Column(db.String(15), nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def get_user_by_username(self):
        return