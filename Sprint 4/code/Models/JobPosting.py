from db import db
from datetime import datetime

# Relational Table b/w Employer and Job Posting (employer Id and jobposting Id)
job_emp = db.Table('job_emp',
    db.Column('job_id', db.Integer, db.ForeignKey('jobposting.id'), primary_key=True),
    db.Column('emp_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

# Model for the Job Posting, and its respective attributes
class JobPosting(db.Model):
    __tablename__ = 'jobposting'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    startDate = db.Column(db.DateTime, nullable=False)
    endDate = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    jobType = db.Column(db.String(10), nullable=False)

    createdByEmployer = db.relationship('User',secondary='job_emp')

    def __init__(self, title, description,startDate,endDate,location,jobType):
      
        self.title = title.lower()
        self.description = description.lower()
        self.location = location.lower()
        self.jobType = jobType.lower()
        self.startDate = datetime.strptime(startDate,"%m/%d/%Y")
        self.endDate =  datetime.strptime(endDate,"%m/%d/%Y")

    # saving the record to db
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # getting the all jobs
    @classmethod
    def get_all_jobs(cls):
        return cls.query.all()
    
    # getting an individual job posting basis on id
    @classmethod
    def get_job_by_id(cls, id_):
        return cls.query.filter_by(id=id_).first()
