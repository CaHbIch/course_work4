from marshmallow import Schema, fields
from sqlalchemy import Column, String

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genre'

    name = Column(String(100), unique=True, nullable=False)


class GenreSchema(Schema):
    name = fields.Str()
