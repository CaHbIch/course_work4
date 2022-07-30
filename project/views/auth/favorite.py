from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service, auth_service, movie_service, favorite_service
from project.dao.models.movie import MovieSchema
from project.tools.security import decode_token

api = Namespace('favorites')


@api.route('/movies/')
class FavouritesViews(Resource):
    def get(self):
        """
         Получает информацию, что добавлено в избранное
        """
        token = request.headers["Authorization"].split("Bearer ")[-1]
        uid = decode_token(token)["id"]
        return favorite_service.get_item(uid), 200


@api.route('/movies/<int:movie_id>/')
class FavoritesView(Resource):
    def post(self, movie_id):
        """Добавить фильм к пользователю в Избранное."""
        # передаем токен пользователя
        token = request.headers["Authorization"].split("Bearer ")[-1]
        access_token = decode_token(token)["id"]
        # Получаем фильм по ID
        movie_d = movie_service.get_item(movie_id)
        # Передаем фильм и токен
        favorite_service.add_favorite(movie_d, access_token)
        return "", 204
