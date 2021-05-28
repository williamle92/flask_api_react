from app import db
from datetime import datetime


class Products(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300))
    amount = db.Column(db.Float(), nullable=False)
    image = db.Column(db.String())
    created = db.Column(db.DateTime(), default=datetime.utcnow)


    def __init__(self, title, description, amount, image):
        self.title = title
        self.description = description
        self.amount = amount
        self.image = image

    def __repr__(self):
        return f"<{self.title} {self.amount} {self.id}>"

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'amount' : self.amount,
            'image' : self.image,
            'created': self.created
        }


