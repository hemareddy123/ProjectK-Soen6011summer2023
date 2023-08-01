#%%
import sys
import os

# Get the absolute path of the directory containing 'app.py'
app_dir = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.join(app_dir, '..')
sys.path.insert(0, app_path)


#%%
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from Models.User import User

# Step 1: Define the SQLAlchemy model
Base = declarative_base()

# Step 2: Create a session
engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
session = Session()

#%%
# Step 3: Use the delete() method on a query object
# Delete users with the name 'John'
session.query(User).filter(User.id.in_(range(9, 31)) | User.id.in_(5,6,7)).delete()

#%%
# Step 4: Commit the changes to the database
session.commit()