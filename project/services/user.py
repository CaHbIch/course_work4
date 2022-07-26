from typing import Optional

from project.dao.base import BaseDAO
from project.dao.models.user import User
from project.exceptions import ItemNotFound
from project.tools.security import generate_password_hash


class UsersService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'User with pk={pk} not exists.')

    def get_all(self, status: Optional[str] = None, page: Optional[int] = None) -> list[User]:
        return self.dao.get_all(page=page, status=status)

    def get_user_by_email(self, email: str) -> User:
        return self.dao.get_user_by_email(email)

    def create(self, data):
        data["password"] = generate_password_hash(data.get("password"))
        return self.dao.create(**data)

    def update(self, data: dict):
        data["password"] = generate_password_hash(data.get("password"))
        return self.dao.update(data)
