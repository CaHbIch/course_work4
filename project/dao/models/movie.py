from marshmallow import Schema, fields

from sqlalchemy import Column, String, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from project.dao.models.director import DirectorSchema
from project.dao.models.genre import GenreSchema
from project.setup.db import models


class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(255))
    description = Column(String(255))
    trailer = Column(String(255))
    year = Column(Integer)
    rating = Column(Float)
    genre_id = Column(Integer, ForeignKey("genres.id"))
    director_id = Column(Integer, ForeignKey("directors.id"))

    genre = relationship("Genre")
    director = relationship("Director")


class MovieSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
    genre = fields.Nested(GenreSchema)
    director = fields.Nested(DirectorSchema)
