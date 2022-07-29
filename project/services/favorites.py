from project.dao import FavoritesDAO
from project.exceptions import ItemAlreadyExists


class FavoriteService:
    def __init__(self, dao: FavoritesDAO) -> None:
        self.dao = dao

    def add_favourite(self, user_id, movie_id) -> None:
        """
        Добавить фильм в избранное пользователя
        :raises: ItemAlreadyExists: если фильм уже в избранном
        """

        data = {
            'user_id': user_id,
            'movie_id': movie_id
        }
        if self.dao.get_favorite(user_id, movie_id):
            raise ItemAlreadyExists

        self.dao.get_all(data)
