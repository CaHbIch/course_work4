from flask import request
from flask_restx import Namespace, Resource

from project.container import movie_service, user_service, favorite_service, favorite_dao
from project.dao.models.movie import MovieSchema
from project.tools.security import decode_token, auth_required

api = Namespace('favorites')


@api.route('/movies/')
class FavouritesViews(Resource):
    @api.doc(description='Избранное пользователя')
    @api.response(200, 'Добавлено')
    @api.response(404, 'Нет такого фильма')
    def get(self):
        rs = favorite_service.get_user_favorites()
        res = MovieSchema(many=True).dump(rs)
        return res, 200


@api.route('/movies/<int:movie_id>/')
class FavouriteView(Resource):
    def post(self, movie_id):
        # Передаем токен пользователя
        token = request.headers["Authorization"].split("Bearer ")[-1]
        access_token = decode_token(token)["id"]

        # Добавляем фильм в избранное
        favorite_service.add_favourite(access_token, movie_id)
        return "", 200

    def delete(self, movie_id):
        # Передаем токен пользователя
        token = request.headers["Authorization"].split("Bearer ")[-1]
        access_token = decode_token(token)["id"]

        # Удаляем из избранного
        favorite_service.delete_favourite(access_token, movie_id)
        return "", 200
