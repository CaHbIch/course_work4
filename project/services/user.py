from typing import Optional

from flask import current_app

from project.dao import UsersDAO
from project.dao.models.user import User
from project.exceptions import ItemNotFound
from project.tools.security import generate_password_hash, decode_token


class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    @property
    def _items_per_page(self) -> int:
        return current_app.config['ITEMS_PER_PAGE']

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

    def update_user(self, data, access_token):
        if user := self.get_item(access_token):
            if 'name' in data:
                user.name = data['name']
            if 'surname' in data:
                user.surname = data['surname']
            if 'favourite_genre' in data:
                user.favorite_genre = data['favourite_genre']
            self.dao.update(user)
