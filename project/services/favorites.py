from project.dao import FavoritesDAO
from project.dao.models.movie import Movie
from project.exceptions import ItemNotFound


class FavoriteService:
    def __init__(self, dao: FavoritesDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Movie with pk={pk} not exists.')

    def add_favorite(self, movie_d, access_token):
        if favorite := self.get_item(access_token):
            return self.dao.update(favorite, movie_d)

