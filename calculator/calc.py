from telebot import TeleBot
from telebot import types
from calculator_real import math_string_to_list
from calculator_complex import math_complex_to_list
from logger import log
import telebot.types
import config
bot = TeleBot(config.TOKEN)


result = ""
old_result = ""


keyboard = types.InlineKeyboardMarkup()

keyboard.row(telebot.types.InlineKeyboardButton("C", callback_data="C"),
             telebot.types.InlineKeyboardButton("<<", callback_data="<<"),
             telebot.types.InlineKeyboardButton("(", callback_data="("),
             telebot.types.InlineKeyboardButton(")", callback_data=")"),
             telebot.types.InlineKeyboardButton("complex", callback_data="complex"))

keyboard.row(telebot.types.InlineKeyboardButton("1", callback_data="1"),
             telebot.types.InlineKeyboardButton("2", callback_data="2"),
             telebot.types.InlineKeyboardButton("3", callback_data="3"),
             telebot.types.InlineKeyboardButton("+", callback_data="+"))

keyboard.row(telebot.types.InlineKeyboardButton("4", callback_data="4"),
             telebot.types.InlineKeyboardButton("5", callback_data="5"),
             telebot.types.InlineKeyboardButton("6", callback_data="6"),
             telebot.types.InlineKeyboardButton("-", callback_data="-"))

keyboard.row(telebot.types.InlineKeyboardButton("7", callback_data="7"),
             telebot.types.InlineKeyboardButton("8", callback_data="8"),
             telebot.types.InlineKeyboardButton("9", callback_data="9"),
             telebot.types.InlineKeyboardButton("*", callback_data="*"))

keyboard.row(telebot.types.InlineKeyboardButton("i", callback_data="i"),
             telebot.types.InlineKeyboardButton(",", callback_data="."),
             telebot.types.InlineKeyboardButton("0", callback_data="0"),
             telebot.types.InlineKeyboardButton("=", callback_data="="),
             telebot.types.InlineKeyboardButton("/", callback_data="/"))


@bot.message_handler(commands=["start"])
def start(msg: telebot.types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    com_num = types.KeyboardButton("/complex")
    real_num = types.KeyboardButton("/real")
    logic = types.KeyboardButton("/log")
    markup.add(com_num, real_num, logic)
    bot.send_message(chat_id=msg.from_user.id, text="Выберете пункт из меню:", reply_markup=markup)


@bot.message_handler(commands=["real"])
def real(msg: telebot.types.Message):
    global result
    bot.send_message(chat_id=msg.from_user.id, text="Для работы с комплексными числами, "
                                                    "введите выражение вида: (5-2i)+(4-1i)"
                                                    " и 'complex' для вывода")
    if result == "":
        bot.send_message(chat_id=msg.from_user.id, text="0", reply_markup=keyboard)
    else:
        bot.send_message(chat_id=msg.from_user.id, text=result, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def result_callback(query):
    global result, old_result
    data = query.data
    if data == "C":
        result = ""
    elif data == "=":
        result = math_string_to_list(result)
    elif data == "complex":
        result = math_complex_to_list(result)
    elif data == "<<":
        result = result[:-1]
    else:
        result += data
    if result != old_result:
        if result == "":
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id,
                                  text="0", reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id,
                                  text=result, reply_markup=keyboard)
    old_result = result


@bot.message_handler(commands=["log"])
def send_log(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Calculator log")
    bot.send_document(chat_id=msg.from_user.id, document=open("files/logger.csv", 'rb'))


bot.polling(none_stop=True)
