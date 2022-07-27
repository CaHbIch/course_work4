from flask import request
from flask_restx import Namespace, Resource

api = Namespace('/favorites/movies')


@api.route('/<int:movie_id>')
class FavoritesView(Resource):
    def post(self):
        """Добавляет фильм к пользователю избранное"""
        req_json = request.json
        return req_json
