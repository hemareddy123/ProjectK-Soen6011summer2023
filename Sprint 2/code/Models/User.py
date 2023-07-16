from db import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __init__(self, username, password):
        # Con.__init__(self)
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


