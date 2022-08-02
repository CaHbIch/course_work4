from typing import List

from flask_restx import abort

from project.dao import FavoritesDAO
from project.dao.models.favorite import Favorite
from project.exceptions import ItemAlreadyExists, ItemNotFound


class FavoriteService:
    def __init__(self, dao: FavoritesDAO) -> None:
        self.dao = dao

    def add_favourite(self, user_id, movie_id) -> object:
        """ Добавить фильм в избранное пользователя
        :raises ItemAlreadyExists: если фильм уже в избранном"""
        data = {
            'user_id': user_id,
            'movie_id': movie_id
        }
        if self.dao.get_favorite(user_id, movie_id):
            raise ItemAlreadyExists

        return self.dao.create(data)

    def get_user_favorites(self) -> List[Favorite]:
        """ Получает все избранное пользователя"""
        favourites = self.dao.get_user_favorites()
        return favourites

    def delete_favourite(self, user_id, movie_id):
        """ Удаляет все фильмы из избранного """
        favourite = self.dao.get_favorite(user_id, movie_id)

        if not favourite:
            abort(404)

        self.dao.delete(favourite[0].id)
