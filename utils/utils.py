import logging

from exceptions.db_exceptions import UserAlreadyExists
from exceptions.moodle_exceptions import MoodleWrongCredentials
# from loader import scheduler

from models import db
from moodle_new.User import User
from repository.UserRepository import UserRepository


logger = logging.getLogger(__name__)


async def add_user(chat_id, user_login, user_pswd):
    user = db.User(chat_id, user_login, user_pswd)

    # Authorisation at moodle-based platform (dl.nure.ua)
    # if only user had not already been added to the database
    if not await UserRepository.exists(user):
        try:
            User(user_login, user_pswd)
        except MoodleWrongCredentials as e:
            logger.error(e)
            raise

    # adding user to database or raising exception if it does not exist
    try:
        await UserRepository.save(user)
    except UserAlreadyExists as e:
        logger.error(e)
        raise


async def login(chat_id):
    stored_user = await UserRepository.get(chat_id)
    moodle_user = User(stored_user.login, stored_user.pswd)
    return moodle_user


async def show_stored_users():
    return await UserRepository.all()













