from project.dao.base import BaseDAO
from project.dao.models.favorite import Favorite
from project.dao.models.movie import Movie


class FavoritesDAO(BaseDAO[Favorite]):
    __model__ = Favorite

    def get_favorite(self, user_id, movie_id) -> list:
        """ Получить фильм из избранного """
        data = self._db_session.query(Favorite) \
            .filter(Favorite.user_id == user_id, Favorite.movie_id == movie_id) \
            .all()
        return data

    def get_user_favorites(self) -> list:
        """ Получает закладки у пользователя"""
        data = self._db_session.query(Movie).join(Favorite).all()
        return data

    def create(self, data: dict) -> object:
        """ Добавляет фильм в базу"""
        item = self.__model__(**data)
        self._db_session.add(item)
        self._db_session.commit()
        return item

    def delete(self, uid):
        item = self.__model__(uid)
        self._db_session.delete(item)
        self._db_session.commit()
