from app import db
from sqlalchemy.orm import relationship

class OmikuziTitle(db.Model):
    __tablename__ = 'OmikuziTitle'
    id = db.Column(db.Integer, primary_key=True)
    main_title = db.Column(db.Text)
    OmikuziContent = relationship("OmikuziContent", backref="OmikuziTitle")

class OmikuziContent(db.Model):
    __tablename__ = 'OmikuziContent'
    main_title_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    omikuzi_main_title = relationship("OmikuziTitle")

def init():
    db.create_all()