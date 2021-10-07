import logging

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import BOT_TOKEN, LOGFILE


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


scheduler = AsyncIOScheduler()
# dp.middleware.setup(LoggingMiddleware())
# logging.basicConfig(level=logging.INFO, filename=LOGFILE, filemode='w')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
