import logging

from exceptions.db_exceptions import UserAlreadyExists
from exceptions.moodle_exceptions import MoodleWrongCredentials
# from loader import scheduler
from loader import bot

from models import db
from moodle_new.Timetable import Timetable
from moodle_new.User import User
from repository.UserRepository import UserRepository
from utils.scheduler import view_jobs, get_users_timetable

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


async def get_all_users_ids():
    users = await show_stored_users()
    ids = []
    for user in users:
        ids.append(user.chat_id)
    return ids


async def send_all_users():
    users_ids = await get_all_users_ids()
    for id in users_ids:
        timetable = await get_users_timetable(id)

        for el in timetable.view():
            await bot.send_message(id, el)












