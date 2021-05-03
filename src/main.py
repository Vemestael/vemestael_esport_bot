from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from easysettings import EasySettings

import esport_matches_api as esapi

games = ["dota2", "csgo"]
# pandascore.co token
token = 'TOKEN'

# telegram bot token
updater = Updater(token='TOKEN')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename="info.log",
                    level=logging.INFO)
settings = EasySettings(".conf")


def get_matches_info(update, context):
    command = update.message.text.split(' ')[0]
    page_size = int(settings.get('matches_number', 3))

    if command == "/past_matches":
        get_matches = esapi.get_past_matches
    elif command == "/running_matches":
        get_matches = esapi.get_running_matches
    elif command == "/upcoming_matches":
        get_matches = esapi.get_upcoming_matches

    if len(context.args):
        if context.args[0].lower() in "dota2":
            game = games[0]
        elif context.args[0].lower() in "csgo cs:go":
            game = games[1]
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="the specified game is not in the list")
            return
        response = get_matches(game, token, page_size)
    else:
        response = list()
        response += get_matches(games[0], token, page_size)
        response += get_matches(games[1], token, page_size)

    for match in response:
        response_text = ""
        for key in match:
            response_text += str(key) + "\n"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=response_text)


def get_settings(update, context):
    settings_list = [
        "/get_number_of_matches - Get the number of displayed matches",
        "/set_number_of_matches - Set the number of displayed matches"
    ]
    response_text = str()
    for setting in settings_list:
        response_text += setting + '\n'
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=response_text)


def get_number_of_matches(update, context):
    matches_number = settings.get('matches_number', 0)
    if matches_number:
        response_text = f"the number of displayed matches: {matches_number}"
    else:
        response_text = f"this setting is not set, default value = 3"
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=response_text)


def set_number_of_matches(update, context):
    try:
        matches_number = context.args[0]
        settings.set('matches_number', matches_number)
        settings.save()
        response_text = "the setting was set successfully"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=response_text)
    except:
        response_text = "invalid entered value"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=response_text)


matches_handler = CommandHandler(
    ['past_matches', 'running_matches', 'upcoming_matches'], get_matches_info)
dispatcher.add_handler(matches_handler)

settings_handler = CommandHandler(
    'settings', get_settings)
dispatcher.add_handler(settings_handler)

get_matches_number_handler = CommandHandler(
    'get_number_of_matches', get_number_of_matches)
dispatcher.add_handler(get_matches_number_handler)

set_matches_number_handler = CommandHandler(
    'set_number_of_matches', set_number_of_matches)
dispatcher.add_handler(set_matches_number_handler)

updater.start_polling()

updater.idle()
