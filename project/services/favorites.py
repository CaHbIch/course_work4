from project.dao import FavoritesDAO


class FavoriteService:
    def __init__(self, dao: FavoritesDAO) -> None:
        self.dao = dao

    def create(self, movie):
        return self.dao.create(movie)
