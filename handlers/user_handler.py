from aiogram import types
from utils import utils
from loader import dp
from utils.scheduler import view_jobs


@dp.message_handler(commands=['user_add'])
async def add_user(msg: types.Message):
    await utils.add_user(0, 'TEST_LOGIN', 'TEST_PSWD')


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





