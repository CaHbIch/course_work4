from typing import Optional

from project.dao.base import BaseDAO
from project.dao.models.genre import Genre
from project.exceptions import ItemNotFound


class GenresService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Genre:
        if genre := self.dao.get_by_id(pk):
            return genre
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, status: Optional[str] = None, page: Optional[int] = None) -> list[Genre]:
        return self.dao.get_all(page=page, status=status)
