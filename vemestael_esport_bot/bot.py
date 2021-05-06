from os import makedirs
from os.path import exists

from dotenv import dotenv_values
from easysettings import EasySettings

import vemestael_esport_bot.esport_matches_api as esapi

games = ["dota2", "csgo"]

env_values = dotenv_values(".env")
# pandascore.co token
token = env_values["PANDASCORE_TOKEN"]

def start(update, context):
    start_text = """Hi! This bot provides information on eSports matches.\n
Information is currently available on two games: Dota 2 and CS:GO.\n
By default, the bot displays information for two games at once.\n
If you want to get data on a particular game, add its name after the command, as /command game_name.\n
To get match information for a team, add the team name after the command, as /command team_name.\n
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text=start_text)

def get_matches_info(update, context):
    command = update.message.text.split(' ')[0]

    if not exists(f"configs/{update.message.chat.id}"):
        makedirs(f"configs/{update.message.chat.id}")
    settings = EasySettings(f"configs/{update.message.chat.id}/.conf")
    page_size = int(settings.get('matches_number', 3))
    days_range = int(settings.get('days_range', 1))

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
        response = get_matches(game, token, page_size, days_range)
    else:
        response = list()
        response += get_matches(games[0], token, page_size, days_range)
        response += get_matches(games[1], token, page_size, days_range)

    for match in response:
        response_text = ""
        for key in match:
            response_text += str(key) + "\n"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=response_text, disable_web_page_preview=True)


def get_team_matches_info(update, context):
    command = update.message.text.split(' ')[0]

    if not exists(f"configs/{update.message.chat.id}"):
        makedirs(f"configs/{update.message.chat.id}")
    settings = EasySettings(f"configs/{update.message.chat.id}/.conf")
    page_size = int(settings.get('matches_number', 3))
    days_range = int(settings.get('days_range', 1))

    if command == "/team_past_matches":
        get_team_matches = esapi.get_team_past_matches
    elif command == "/team_upcoming_matches":
        get_team_matches = esapi.get_team_upcoming_matches

    if not len(context.args):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please specify the team name")
    team = context.args[0].lower()
    response = get_team_matches(team, token, page_size, days_range)

    for match in response:
        response_text = ""
        for key in match:
            response_text += str(key) + "\n"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=response_text, disable_web_page_preview=True)


def get_settings(update, context):
    settings_list = [
        "/get_number_of_matches - Get the number of displayed matches",
        "/set_number_of_matches - Set the number of displayed matches",
        "/get_days_range - Get get the range of days to sample"
        "/set_days_range - Set get the range of days to sample"
    ]
    response_text = str()
    for setting in settings_list:
        response_text += setting + '\n'
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=response_text)


def get_number_of_matches(update, context):
    if not exists(f"./configs/{update.message.chat.id}"):
        makedirs(f"./configs/{update.message.chat.id}")
    settings = EasySettings(f"./configs/{update.message.chat.id}/.conf")
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

        if not exists(f"configs/{update.message.chat.id}"):
            makedirs(f"configs/{update.message.chat.id}")
        settings = EasySettings(f"configs/{update.message.chat.id}/.conf")
        settings.set('matches_number', matches_number)
        settings.save()
        response_text = "the setting was set successfully"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=response_text)
    except:
        response_text = "invalid entered value"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=response_text)


def get_days_range(update, context):
    if not exists(f"./configs/{update.message.chat.id}"):
        makedirs(f"./configs/{update.message.chat.id}")
    settings = EasySettings(f"./configs/{update.message.chat.id}/.conf")
    days_range = settings.get('days_range', 0)
    if days_range:
        response_text = f"the range of days to sample: {days_range}"
    else:
        response_text = f"this setting is not set, default value = 1"
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=response_text)


def set_days_range(update, context):
    try:
        days_range = context.args[0]

        if not exists(f"configs/{update.message.chat.id}"):
            makedirs(f"configs/{update.message.chat.id}")
        settings = EasySettings(f"configs/{update.message.chat.id}/.conf")
        settings.set('days_range', matches_number)
        settings.save()
        response_text = "the setting was set successfully"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=response_text)
    except:
        response_text = "invalid entered value"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=response_text)
