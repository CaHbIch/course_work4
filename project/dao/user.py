from typing import Optional

from flask_sqlalchemy import BaseQuery

from project.dao.base import BaseDAO
from project.dao.models.user import User


class UsersDAO(BaseDAO[User]):
    __model__ = User

    def get_user_by_email(self, email: Optional[str]):
        """Получить пользователя по email"""
        stmt: BaseQuery = self._db_session.query(self.__model__)
        return stmt.filter(self.__model__.email == email).first()

    def create(self, **kwargs) -> bool:
        """" Добавляет пользователя """
        try:
            self._db_session.add(self.__model__(**kwargs))
            self._db_session.commit()
            return True
        except Exception as e:
            print(f"Не удалось зарегистрировать пользователя\n{e}")
            self._db_session.rollback()
            return False

    def update(self, kwargs):
        """ Обновляет данные пользователя """
        try:
            self._db_session.add(kwargs)
            self._db_session.commit()
        except Exception as e:
            print(f"Не удалось обновить пользователя\n{e}")
            self._db_session.rollback()
