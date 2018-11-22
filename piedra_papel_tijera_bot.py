from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from pipati import PiPaTi

JUGADAS = dict()

BOTON_PIEDRA = "Piedra"
BOTON_PAPEL = "Papel"
BOTON_TIJERA = "Tijera"

BOTON_JUGAR = "Jugar"
CALLBACK_JUGAR = "9"


def botonera_juego():
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(BOTON_PIEDRA, callback_data=PiPaTi.PIEDRA)],
            [InlineKeyboardButton(BOTON_PAPEL, callback_data=PiPaTi.PAPEL)],
            [InlineKeyboardButton(BOTON_TIJERA, callback_data=PiPaTi.TIJERA)],
        ]
    )


def botonera_volver():
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(BOTON_JUGAR, callback_data=CALLBACK_JUGAR)]]
    )


def jugar(bot, update):
    chat_id = update.message.chat_id
    JUGADAS[chat_id] = PiPaTi()
    bot.send_message(chat_id, "Piedra, papel o tijera?!", reply_markup=botonera_juego())


def button(bot, update):
    query = update.callback_query
    chat_id = query.message.chat_id

    if query.data == CALLBACK_JUGAR:
        JUGADAS[chat_id] = PiPaTi()
        bot.send_message(
            chat_id, "Piedra, papel o tijera?!", reply_markup=botonera_juego()
        )

    if query.data in PiPaTi.OPCIONES:
        message_id = query.message.message_id
        resultado = JUGADAS[chat_id].vs_maquina(query.data)

        bot.edit_message_text(
            text=resultado,
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=botonera_volver(),
        )
