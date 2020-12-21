from app import db

class OmikuziContent(db.Model):
    __tablename__ = 'OmikuziContent'
    id = db.Column(db.Integer, primary_key=True)
    main_title = db.Column(db.Text)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

def init():
    db.create_all()