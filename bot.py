import os
import logging

from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import (
    Dispatcher,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
)
from piedra_papel_tijera_bot import jugar, button

token = os.getenv("PIPATI_TOKEN")
bot = Bot(token)
dispatcher = Dispatcher(bot, None, workers=0)
dispatcher.add_handler(CommandHandler("start", jugar))
dispatcher.add_handler(MessageHandler(Filters.text, jugar))
dispatcher.add_handler(CallbackQueryHandler(button))

app = Flask(__name__)

logger = logging.getLogger("PipatiBot")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
logger.setLevel(logging.DEBUG)
shandler = logging.StreamHandler()
shandler.setFormatter(formatter)
logger.addHandler(shandler)


@app.errorhandler(500)
def _500(error):
    logger.error("Server error: %s", error)


@app.route('/pipati', methods=['POST'])
def pipati():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"
