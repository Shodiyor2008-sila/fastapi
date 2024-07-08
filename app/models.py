from sqlalchemy import String,Column,Integer,Boolean,ForeignKey
from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP,DATE
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    title = Column(String(45),nullable=False)
    content = Column(String(45),nullable=False)
    published = Column(String(10),default=True)
    created_at = Column(DATE,nullable=False,default='2019-09-09')
    user_id = Column(Integer,ForeignKey('users.id',ondelete='CASCADE'),nullable=False)
    user = relationship('Users')
    

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    email = Column(String(45),nullable=False,unique=True)
    password = Column(String(10000),nullable = False)
    created_at = Column(DATE,nullable=False,default='2019-09-09')
    # post = relationship('Post')
class Vote(Base):
    __tablename__ = 'votes'
    user_id = Column(Integer,ForeignKey('users.id',ondelete='CASCADE'),primary_key=True)
    post_id = Column(Integer,ForeignKey('posts.id',ondelete='CASCADE'),primary_key=True)


