from db import db
from sqlalchemy import Text

class Chat(db.Model):
    __tablename__ = 'chat'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    empId = db.Column(db.Integer,nullable=False)
    studId = db.Column(db.Integer,nullable=False)
    text = db.Column(Text,nullable=False)
    initater = db.Column(db.String(10), nullable=False)

    def __init__(self,empId, studId, text,initater):
        self.empId = empId
        self.studId = studId
        self.text = text
        self.initater = initater
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_chat_by_empId_studId(cls, empId_, studId_):
        return cls.query.filter(cls.empId == empId_, cls.studId == studId_).all()
