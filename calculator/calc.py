from telebot import TeleBot
from telebot import types
from calculator_real import math_string_to_list
from calculator_complex import math_complex_to_list
from logger import log
import telebot.types
import config
bot = TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def start(msg: telebot.types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    com_num = types.KeyboardButton("/complex")
    real_num = types.KeyboardButton("/real")
    logic = types.KeyboardButton("/log")
    markup.add(com_num, real_num, logic)
    bot.send_message(chat_id=msg.from_user.id, text="Click complex or real numbers "
                                                    "or log to download the log", reply_markup=markup)


@bot.message_handler(commands=["real"])
def real(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Enter digits to calculate, expression with brackets are supported")
    bot.register_next_step_handler(callback=real_calc, message=msg)


def real_calc(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=math_string_to_list(msg.text))
    bot.send_message(chat_id=msg.from_user.id, text="/start")
    log(msg.text, math_string_to_list(msg.text))


@bot.message_handler(commands=["complex"])
def complex_(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Enter complex digits to calculate, "
                                                    "for example (1 + 1i) + (5 - 2i)")
    bot.register_next_step_handler(callback=complex_calc, message=msg)


def complex_calc(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=math_complex_to_list(msg.text))
    bot.send_message(chat_id=msg.from_user.id, text="/start")
    log(msg.text, math_complex_to_list(msg.text))


@bot.message_handler(commands=["log"])
def send_log(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Calculator log")
    bot.send_document(chat_id=msg.from_user.id, document=open("files/logger.csv", 'rb'))


bot.polling(none_stop=True)
