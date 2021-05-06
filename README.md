# Vemestael eSport bot

Telegram bot for viewing information on eSports matches

## Installation
- Clone this git repository.
```
$ git clone https://github.com/Vemestael/vemestael_esport_bot.git
```
- Change directory
```
$ cd vemestael_esport_bot
```
- Create a virtual environment
```
$ python -m venv .
```
- Activate a virtual environment
#### Linux
```
$ source bin/activate
```
#### Windows
```
$ script\activate
```
- Install requirements with pip
```
$ pip install -r requirements.txt
```
- Create environment file
#### Linux
```
$ cp .env.example .env
```
#### Windows
```
$ copy .env.example .env
```

## Configuration
- Add [api keys](#configuration-values) to .env file.
- For ease of use, set next the list of commands for bot:
  - past_matches - show info by past matches in esport
  - running_matches - show info by running matches in esport
  - upcoming_matches - show info by upcoming matches in esport
  - team_past_matches - show info by team past matches
  - team_upcoming_matches - show info by team upcoming matches
  - settings - show available settings

### Configuration Values
- `PANDASCORE_TOKEN` - Get it on [PandaScore.co](https://pandascore.co/)
- `TELEGRAM_BOT_TOKEN` - Get it by contacting to [BotFather](https://t.me/botfather) ([guilde](https://core.telegram.org/bots#6-botfather))

## Usage
```
python -m vemestael_esport_bot
```

## License

This project is licensed under the [MIT License](LICENSE).

## Thanks
- [PandaScore](https://pandascore.co/)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)