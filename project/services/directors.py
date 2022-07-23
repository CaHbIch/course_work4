from typing import Optional

from project.dao.base import BaseDAO
from project.dao.models.director import Director

from project.exceptions import ItemNotFound


class DirectorsService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Director:
        if director := self.dao.get_by_id(pk):
            return director
        raise ItemNotFound(f'Director with pk={pk} not exists.')

    def get_all(self, status: Optional[str] = None, page: Optional[int] = None) -> list[Director]:
        return self.dao.get_all(page=page, status=status)
