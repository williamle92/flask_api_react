from app import db
from datetime import datetime
from app.blueprints.auth.models import User


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title=None, body=None, user_id=None):
        self.title = title
        self.body = body
        self.user_id = user_id

    def __repr__(self):
        return f'<Post | {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'date_created': self.date_created,
            'user_id': self.user_id
        }

    def from_dict(self, data):
        for field in ['title', 'body', 'user_id']:
            if field in data:
                setattr(self, field, data[field])

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()        