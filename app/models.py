from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

class OmikuziTitle(db.Model):
    __tablename__ = 'OmikuziTitle'
    id = db.Column(db.Integer, primary_key=True)
    main_title = db.Column(db.Text)
    omikuzicontents = relationship("OmikuziContent", backref="OmikuziTitle")
#テーブル間の紐付けをしている
    def __init__(self, main_title=None):
        self.main_title = main_title

    def __repr__(self):
        return '<Title %r>' % (self.main_title)

class OmikuziContent(db.Model):
    __tablename__ = 'OmikuziContent'
    id = db.Column(db.Integer, primary_key=True)
    OmikuziTitle_id = Column(Integer, ForeignKey('OmikuziTitle.id'))
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    omikuzititle = relationship("OmikuziTitle")

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key=True)
    user_name = db.Column(String(128), unique=True)
    hashed_password = db.Column(String(128))
    balance = db.Column(db.Integer)

    def __init__(self,user_name=None ,hashed_password=None,balance=None):
        self.user_name = user_name
        self.hashed_password = hashed_password
        self.balance = balance

def init():
    db.create_all()