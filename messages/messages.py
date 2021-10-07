from aiogram.utils.markdown import text, italic, code

from config import URL

need_for_help_message = text('I don\'t understand you, human!\n',
                             code('Use'), '/help')
help_message = f'Just give me your credentials for {URL}'
start_message = f"🤖 Hello, I'm here to mark you present every day at all available classes at {URL}."

enter_login = 'Please enter your login'
enter_pswd = 'Please enter your password'
auth_success = 'Authentication completed successfully. Relax!'
auth_button = 'Authentication'

user_already_exists = 'You are already logged in'
wrong_moodle_credentials = f'There is no such user at {URL}. Try again'




# need_for_help_message = text('Я не знаю, что с этим делать',
#                              italic('\nЯ просто напомню,'), 'что есть',
#                              code('команда'), '/help')
