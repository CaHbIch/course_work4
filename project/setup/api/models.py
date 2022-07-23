from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})
director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Имя'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Название'),
    'description': fields.String(required=True, max_length=100, example='Описание'),
    'trailer': fields.String(required=True, max_length=100, example='Трейлер'),
    'year': fields.Integer(required=True, max_length=100, example='Год'),
    'rating': fields.Float(required=True, max_length=100, example='Рейтинг'),
})
