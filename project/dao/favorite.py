from project.dao.base import BaseDAO
from project.dao.models.favorite import Favorite
from project.dao.models.movie import Movie


class FavoritesDAO(BaseDAO[Favorite]):
    __model__ = Favorite

    def update(self, *kwargs):
        """ Обновляет данные пользователя """
        try:
            self._db_session.add(*kwargs)
            self._db_session.commit()
        except Exception as e:
            print(f"Не удалось обновить пользователя\n{e}")
            self._db_session.rollback()



    # def get_favorite(self, user_id, movie_id) -> list:
    #     """ Получить фильм из избранного """
    #     data = self._db_session.query(Favorite) \
    #         .filter(Favorite.user_id == user_id, Favorite.movie_id == movie_id) \
    #         .all()
    #     return data
    #
    # def get_user_favorites(self, user_id) -> list:
    #     """ Получает закладки у пользователя"""
    #     data = self._db_session.query(Movie).join(Favorite) \
    #         .filter(Favorite.user_id == user_id, Movie.id == Favorite.movie_id) \
    #         .all()
    #     return data


