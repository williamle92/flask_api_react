
from app import db
import os


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300))
    amount = db.Column(db.Integer, nullable=False)

    def __init__(self, id, title, description, amount):
        self.id = id
        self.title = title
        self.description = description
        self.amount = amount

    def __repr__(self):
        return f"<{self.title} {self.amount} {self.id}>"

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'amount' : self.amount
        }



