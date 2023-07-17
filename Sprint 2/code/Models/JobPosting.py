from db import db

class JobPosting(db.Model):
    __tablename__ = 'job_posting'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(50), nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def get_user_by_username(self):
        return
