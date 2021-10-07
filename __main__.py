import logging

from aiogram import Dispatcher
from aiogram.utils import executor

import models
from loader import dp, logger, scheduler
from utils import utils
import handlers
from utils.scheduler import run_jobs, get_users_timetable


async def startup(dispatcher: Dispatcher):
    """Triggers on startup."""
    await models.db.create_database()
    users = await utils.show_stored_users()
    logger.info(f'Registered {len(users)} users: {users}')
    await run_jobs()

    # timetable = await get_users_timetable()
    # for time, course in timetable.items():
    #     print(time, course.course_info, sep='\t')

async def shutdown(dispatcher: Dispatcher):
    """Triggers on shutdown."""
    logger.info('Bot closed')
    # await bot.close()


if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    scheduler.start()
    executor.start_polling(dp, on_startup=startup, on_shutdown=shutdown)

