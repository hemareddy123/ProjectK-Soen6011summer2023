from db import db
from sqlalchemy import Text

# Model Chat class to store the data into db
class Chat(db.Model):
    __tablename__ = 'chat'

    # Database columns and their respective attributes
    id = db.Column(db.Integer, primary_key=True, unique=True)
    empId = db.Column(db.Integer,nullable=False)
    studId = db.Column(db.Integer,nullable=False)
    text = db.Column(Text,nullable=False)
    initater = db.Column(db.String(10), nullable=False)

    # constructor
    def __init__(self,empId, studId, text,initater):
        self.empId = empId
        self.studId = studId
        self.text = text
        self.initater = initater
        
    # saving the record into db
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # query to fetch the records where employee matches to a student for the chat session
    @classmethod
    def get_chat_by_empId_studId(cls, empId_, studId_):
        return cls.query.filter(cls.empId == empId_, cls.studId == studId_).all()
