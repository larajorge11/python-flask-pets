from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class Pet(db.Model):
    """Model for pet table"""
    __tablename__ = 'pet'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    pet_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(1), nullable=False)

    def __init__(self, pet_name, age, gender):
        self.pet_name = pet_name
        self.age = age
        self.gender = gender

    def __repr__(self):
        return "<Pet_name %r>" % self.pet_name


class PetSchema(ma.Schema):
    class Meta:
        fields = ('id', 'pet_name', 'age', 'gender')
