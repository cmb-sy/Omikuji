from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

class OmikuziTitle(db.Model):
    __tablename__ = 'OmikuziTitle'
    id = db.Column(db.Integer, primary_key=True)
    main_title = db.Column(db.Text)
    omikuzicontents = relationship("OmikuziContent", backref="OmikuziTitle")
    body = db.Column(db.Text)
#テーブル間の紐付けをしている
    def __init__(self, main_title=None,body=None):
        self.main_title = main_title
        self.body = body

    def __repr__(self):
        return '<Title %r>' % (self.main_title)

class OmikuziContent(db.Model):
    __tablename__ = 'OmikuziContent'
    id = db.Column(db.Integer, primary_key=True)
    OmikuziTitle_id = Column(Integer, ForeignKey('OmikuziTitle.id'))
    title = db.Column(db.Text)
    omikuzititle = relationship("OmikuziTitle")

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(128), unique=True)
    hashed_password = Column(String(128))

def init():
    db.create_all()