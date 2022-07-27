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

    def get_user_by_email(self, email: str) -> User:
        return self.dao.get_user_by_email(email)

    def create(self, data):
        data["password"] = generate_password_hash(data.get("password"))
        return self.dao.create(**data)

    def update(self, data: dict):
        data["password"] = generate_password_hash(data.get("password"))
        return self.dao.update(data)

    def update_part(self, data, uid) -> None:
        """Изменить информацию пользователя:  """
        if user := self.dao.get_by_id(uid):
            if 'name' in data:
                user.name = data['name']
            if 'surname' in data:
                 user.surname = data['surname']
            if 'favorite_genre' in data:
                user.favorite_genre = data['favorite_genre']
            self.dao.update(user)
        else:
            raise ItemNotFound(f'User with uid={uid} not exist.')
