from typing import Generic, List, Optional, TypeVar

from flask import current_app
from flask_sqlalchemy import BaseQuery
from sqlalchemy.orm import scoped_session
from werkzeug.exceptions import NotFound

from project.dao.models.user import User
from project.setup.db.models import Base

T = TypeVar('T', bound=Base)


class BaseDAO(Generic[T]):
    __model__ = Base

    def __init__(self, db_session: scoped_session) -> None:
        self._db_session = db_session

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

    def update(self, kwargs: dict):
        """ Обновляет данные пользователя """
        try:
            self._db_session.query(self.__model__.id).update(kwargs)
            self._db_session.commit()
        except Exception as e:
            print(f"Не удалось обновить пользователя\n{e}")
            self._db_session.rollback()

    @property
    def _items_per_page(self) -> int:
        return current_app.config['ITEMS_PER_PAGE']

    def get_by_id(self, pk: int) -> Optional[T]:
        return self._db_session.query(self.__model__).get(pk)

    def get_all(self, page: Optional[int] = None, status: Optional[str] = None) -> List[T]:
        stmt: BaseQuery = self._db_session.query(self.__model__)
        if status == 'new' and page:
            try:
                sort = stmt.order_by(self.__model__.year.desc())
                return sort.paginate(page, self._items_per_page).items
            except:
                return []
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()
