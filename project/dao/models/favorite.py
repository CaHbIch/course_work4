from marshmallow import Schema, fields
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from project.dao.models.movie import MovieSchema
from project.dao.models.user import UserSchema
from project.setup.db import models


class Favorite(models.Base):
    __tablename__ = 'favorites'

    user_id = Column(Integer, ForeignKey("users.id"))
    movie_id = Column(Integer, ForeignKey("movies.id"))
    user = relationship("User")
    movie = relationship("Movie")


class FavoriteSchema(Schema):
    user_id = fields.Int()
    movie_id = fields.Int()
    user = fields.Pluck(UserSchema, 'name')
    movie = fields.Pluck(MovieSchema, 'title')