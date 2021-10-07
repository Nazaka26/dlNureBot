import logging
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from exceptions.moodle_exceptions import MoodleWrongCredentials
from loader import dp
from keyboards.inline.menus import auth_menu
from messages.messages import start_message
from states.AuthStates import AuthStates
from utils import utils

logger = logging.getLogger(__name__)


@dp.message_handler(commands=['admin'])
async def process_start_command(msg: Message):
    await msg.answer(start_message, reply_markup=auth_menu)

# todo: make admin panel
