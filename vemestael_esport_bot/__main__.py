import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import vemestael_esport_bot.bot as bot

# telegram bot token
updater = Updater(token=bot.env_values["TELEGRAM_BOT_TOKEN"])
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename="info.log",
                    level=logging.INFO)

matches_handler = CommandHandler(
    ['past_matches', 'running_matches', 'upcoming_matches'], bot.get_matches_info)
dispatcher.add_handler(matches_handler)

settings_handler = CommandHandler(
    'settings', bot.get_settings)
dispatcher.add_handler(settings_handler)

get_matches_number_handler = CommandHandler(
    'get_number_of_matches', bot.get_number_of_matches)
dispatcher.add_handler(get_matches_number_handler)

set_matches_number_handler = CommandHandler(
    'set_number_of_matches', bot.set_number_of_matches)
dispatcher.add_handler(set_matches_number_handler)


if __name__ == '__main__':
    updater.start_polling()
    print("bot started")
    updater.idle()
    print("bot finished")