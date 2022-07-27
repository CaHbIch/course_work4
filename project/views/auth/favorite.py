from flask import request
from flask_restx import Namespace, Resource

from project.container import favorite_service
from project.tools.security import auth_required

api = Namespace('/favorites/movies')


@api.route('/<int:movie_id>')
class FavoritesView(Resource):
    def post(self, movie_id):
        """Добавляет фильм пользователя в избранное"""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = movie_id
        add_favorite = favorite_service.create(req_json)
        return "", 201, {"location": f"/movies/{add_favorite.id}"}
