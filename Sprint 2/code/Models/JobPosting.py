from db import db
from datetime import datetime

class JobPosting(db.Model):
    __tablename__ = 'jobposting'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    startDate = db.Column(db.DateTime, nullable=False)
    endDate = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    jobType = db.Column(db.String(10), nullable=False)

    def __init__(self, title, description,startDate,endDate,location,jobType):

        self.title = title.lower()
        self.description = description.lower()
        self.location = location.lower()
        self.jobType = jobType.lower()
        self.startDate = datetime.strptime(startDate,"%m/%d/%Y")
        self.endDate =  datetime.strptime(endDate,"%m/%d/%Y")

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_jobs(cls):
        return cls.query.all()
