from aiogram.dispatcher.filters.state import StatesGroup, State


class AuthStates(StatesGroup):
    WAIT_FOR_LOGIN = State()
    WAIT_FOR_PASSWORD = State()
    AUTHORIZED = State()
