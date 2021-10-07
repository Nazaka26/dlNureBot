import os

BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    exit("Error: no token provided")

LOGFILE = 'logs/bot.log'  # logs/bot.log

# Database
DB_URL = 'sqlite:///users.db'

# Module variables to connect to moodle api
URL = 'https://dl.nure.ua'
LOGIN_URL = URL + '/login/index.php'
ENDPOINT = '/webservice/rest/server.php'


encoding = 'utf-8'
HEROKU_APP_NAME = 'dl-nure-bot'

# Webhook
APP_HOST = 'localhost'      # 192.168.1.1XX, or localhost if use nginx
APP_PORT = 3001
USE_WEBHOOK = False
WEBHOOK_HOST = ''           # example.com or ip
WEBHOOK_PATH = ''           # /webhook
WEBHOOK_PORT = 443
SSL_CERT = ''               # path to ssl certificate
SSL_KEY = ''                # path to ssl private key, hide if use nginx proxy_pass

# Webhook init
WEBHOOK_URL = f'https://{WEBHOOK_HOST}:{WEBHOOK_PORT}{WEBHOOK_PATH}'
WEBHOOK_SERVER = {
    'host': APP_HOST,
    'port': APP_PORT,
    'webhook_path': WEBHOOK_PATH,
}
