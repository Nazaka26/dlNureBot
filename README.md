![](https://img.shields.io/badge/Microverse-blueviolet) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/b5122bd0fc5649eebb07a37508e67888)](https://app.codacy.com/gh/cyonii/yes-bot?utm_source=github.com&utm_medium=referral&utm_content=cyonii/yes-bot&utm_campaign=Badge_Grade)

# About YesBot

This project is a telegram bot that interacts with users. The bot `YesBot` acts as a friendly questionnaire that engages users in series of quiz of very random questions.

My idea of this bot was to create a simple friendly and educative companion that helps users overcome boredom by sharing random knowledge.

![](images/butyesbot_screenshot.png)

## Built With

-  Ruby programming language
-  [telegram-bot-ruby](https://github.com/atipugin/telegram-bot-ruby)
-  [Open Trivia Database API](https://opentdb.com)

## Getting Started

To get started you must have a Telegram account and a Telegram API token. To get an API token and also create a bot, log into your Telegram app, search for `BotFather`, initiate a chat with `BotFather` by clickng **"start"** or typing `/start`, then follow subsequent instructions. Learn more [here](https://core.telegram.org/bots#6-botfather)

## Installation

```sh
$ git clone https://github.com/thehamkercat/LunaChatBot
$ cd LunaChatBot
$ pip3 install -U -r requirements.txt
$ cp sample_config.py config.py
```

Edit `config.py` with your own values.
```sh
$ python3 luna.py
```


## Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/TheHamkerCat/LunaChatBot/tree/master)

## Available Commands

-  /start - to start interaction with the bot
-  /quiz - to get a random quiz

## Author

-  GitHub: [@cyonii](https://github.com/cyonii)
-  Twitter: [@theOnuoha](https://twitter.com/theOnuoha)
-  LinkedIn: [Silas Kalu](https://www.linkedin.com/in/cyonii/)


## 📝 License

This project is [MIT](lic.url) licensed.
