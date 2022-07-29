from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service, auth_service, movie_service, favorite_service
from project.dao.models.movie import MovieSchema
from project.tools.security import decode_token

api = Namespace('favorites')

@api.route('/movies/')
class FavouritesViews(Resource):
    def get(self):
        # получаем токен
        token = request.headers["Authorization"].split("Bearer ")[-1]
        email = decode_token(token)["id"]

        # Проверает данные
        email = decode_token(token)
        user_id = user_service.get_user_by_email(email).id

        # результат
        favourites = favorite_service.get_user_favourites(user_id)
        movies_schema = MovieSchema(many=True)
        return movies_schema.dump(favourites)


# @api.route('/movies/<int:movie_id>/')
# class FavoritesView(Resource):
#     def post(self, movie_id):
#         """добавить фильм к пользователю в Избранное."""
#         # получаем токен
#         token = request.headers["Authorization"].split("Bearer ")[-1]
#         access_token = decode_token(token)["id"]
#         # Проверает данные
#         email = auth_service.get_email_from_token(access_token)
#         user_id = user_service.get_by_email(email).id
#         movie_check = movie_service.get_one(movie_id)
#
#         favourite_service.add_favourite(user_id, movie_id)
#         return "", 204
