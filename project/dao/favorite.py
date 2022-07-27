from project.dao.base import BaseDAO
from project.dao.models.favorite import Favorite


class FavoritesDAO(BaseDAO[Favorite]):
    __model__ = Favorite

    def create(self, movie):
        self._db_session.add(movie)
        self._db_session.commit()

