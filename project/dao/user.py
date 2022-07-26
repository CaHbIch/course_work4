from project.dao.base import BaseDAO
from project.dao.models.user import User


class UsersDAO(BaseDAO[User]):
    __model__ = User
