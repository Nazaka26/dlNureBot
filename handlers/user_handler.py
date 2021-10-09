from aiogram import types
from utils import utils
from loader import dp
from utils.scheduler import view_jobs
from utils.utils import send_all_users


@dp.message_handler(commands=['users_all'])
async def add_user(msg: types.Message):
    a = await utils.show_stored_users()
    await msg.reply(a)


@dp.message_handler(commands=['login'])
async def login(msg: types.Message):
    a = await utils.login(msg.chat.id)
    await msg.reply(a)

@dp.message_handler(commands=['jobs'])
async def get_jobs(msg: types.Message):
    a = await view_jobs()
    await msg.reply(a)


@dp.message_handler(commands=['timetable'])
async def get_my_timetable(msg: types.Message):
    id = msg.chat.id
    await msg.reply(id)

@dp.message_handler(commands=['send_jobs'])
async def send_all_jobs(msg: types.Message):

    await send_all_users()
