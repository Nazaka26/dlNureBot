from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from messages.messages import auth_button

auth_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(auth_button, callback_data='auth')
        ]
    ]
)



