from telebot import TeleBot
from telebot import types
from calculator_real import math_string_to_list
import telebot.types
import config
bot = TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def start(msg: telebot.types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    com_num = types.KeyboardButton("/complex")
    real_num = types.KeyboardButton("/real")
    markup.add(com_num, real_num)
    bot.send_message(chat_id=msg.from_user.id, text="Choose complex or real numbers", reply_markup=markup)


@bot.message_handler(commands=["real"])
def real(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Enter digits to calculate, expression with brackets are supported")
    bot.register_next_step_handler(callback=real_calc, message=msg)


def real_calc(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=math_string_to_list(msg.text))
    bot.send_message(chat_id=msg.from_user.id, text="/start")


@bot.message_handler(commands=["complex"])
def complex_(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Enter complex digits to calculate")
    bot.register_next_step_handler(callback=complex_calc, message=msg)


def complex_calc(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=math_string_to_list(msg.text))
    bot.send_message(chat_id=msg.from_user.id, text="/start")


bot.polling(none_stop=True)