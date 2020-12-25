from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class OmikuziTitle(db.Model):
    __tablename__ = 'OmikuziTitle'
    id = db.Column(db.Integer, primary_key=True)
    main_title = db.Column(db.Text)
    # OmikuziContent = relationship("OmzzikuziContent", backref="omikuzititle")
#テーブル間の紐付けをしている

class OmikuziContent(db.Model):
    __tablename__ = 'OmikuziContent'
    main_title_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(128), unique=True)
    hashed_password = Column(String(128))

    def __init__(self, user_name=None, hashed_password=None):
        self.user_name = user_name
        self.hashed_password = hashed_password

    def __repr__(self):
        return '<Name %r>' % (self.user_name)

def init():
    db.create_all()