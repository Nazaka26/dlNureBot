import logging

from typing import List

from exceptions.db_exceptions import UserAlreadyExists, UserDoesNotExist
from models import db

logger = logging.getLogger(__name__)


class UserRepository:

    @classmethod
    async def first(cls) -> db.User:
        """
        :return: First found row
        """
        with await db.get_session() as session:
            return session.query(db.User).first()

    @classmethod
    async def get(cls, id_) -> db.User:
        """
        Find record by the id
        :param id_: the primary key
        :return: result raw
        """
        with await db.get_session() as session:
            return session.query(db.User).get(id_)

    @classmethod
    async def all(cls) -> List[db.User]:
        """
        :return:  All content from table object
        """
        with await db.get_session() as session:
            return session.query(db.User).all()

    @classmethod
    async def save(cls, user: db.User) -> db.User:
        """
        Saves the user to the current entity db.
        :return: user info
        """

        if await cls.exists(user):
            raise UserAlreadyExists

        # TODO async with
        with await db.get_session() as session:
            session.add(user)
            session.commit()

        logger.info('user added to database')
        return user

    @classmethod
    async def exists(cls, user: db.User):
        existing_user = await cls.get(user.chat_id)
        if existing_user:
            return True
        return False

    @classmethod
    async def update(cls, user: db.User, **kwargs):
        # todo synchronize_session = False
        """
        Persists changes to database.
        :param user: user to be updated
        :param kwargs: field-value pairs to be updated
        :return:
        """
        if await cls.exists(user):
            raise UserDoesNotExist

        for field, value in kwargs.items():
            setattr(user, field, value)
        with await db.get_session() as session:
            session.commit()

    @classmethod
    async def delete(cls, user: db.User):
        """
        Removes the model from the User session and mark for deletion.
        :param user:
        :return:
        """
        if await cls.exists(user):
            raise UserDoesNotExist

        with await db.get_session() as session:
            session.delete(user)
            session.commit()
