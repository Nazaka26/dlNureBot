import logging
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ParseMode, ContentType
from exceptions.db_exceptions import UserAlreadyExists
from exceptions.moodle_exceptions import MoodleWrongCredentials
from loader import dp
from keyboards.inline.menus import auth_menu
from messages.messages import start_message, auth_success, enter_login, enter_pswd, help_message, user_already_exists, \
    wrong_moodle_credentials, need_for_help_message
from states.AuthStates import AuthStates
from utils import utils

logger = logging.getLogger(__name__)


@dp.message_handler(commands=['start'])
async def process_start_command(msg: Message):
    # todo: if user exists
    await msg.answer(start_message, reply_markup=auth_menu)


@dp.message_handler(commands=['help'])
async def process_start_command(msg: Message):
    await msg.answer(help_message, reply_markup=auth_menu)


@dp.callback_query_handler(text='auth', state=None)
async def auth_button(call: CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.answer(enter_login)
    await AuthStates.WAIT_FOR_LOGIN.set()


@dp.message_handler(state=AuthStates.WAIT_FOR_LOGIN)
async def get_login(msg: Message, state: FSMContext):
    login = msg.text
    await state.update_data(login=login)

    await msg.answer(enter_pswd)
    await AuthStates.WAIT_FOR_PASSWORD.set()


@dp.message_handler(state=AuthStates.WAIT_FOR_PASSWORD)
async def get_password(msg: Message, state: FSMContext):
    password = msg.text
    await state.update_data(password=password)

    auth_data = await state.get_data()
    await state.reset_state()

    chat_id = msg.chat.id
    login = auth_data['login']
    password = auth_data['password']
    try:
        await utils.add_user(chat_id, login, password)
        await msg.answer(auth_success)
    except MoodleWrongCredentials as e:
        logger.error(e)
        await msg.answer(wrong_moodle_credentials, reply_markup=auth_menu)
    except UserAlreadyExists as e:
        logger.error(e)
        await msg.answer(user_already_exists)


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: Message):
    await msg.reply(need_for_help_message, parse_mode=ParseMode.MARKDOWN)
