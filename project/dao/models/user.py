from marshmallow import Schema, fields
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


class User(models.Base):
    __tablename__ = 'users'

    email = Column(String(20), unique=True, nullable=False)
    name = Column(String(20))
    surname = Column(String(20))
    password = Column(String(10), nullable=False)
    favorite_genre = Column(String(200), ForeignKey("genres.id"))
    genre = relationship("Genre")


class UserSchema(Schema):
    email = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    password = fields.Str()
    favorite_genre = fields.Str()
