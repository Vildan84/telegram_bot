import random
import telebot.types
from telebot import TeleBot
from telebot import types
import config
bot = TeleBot(config.TOKEN)

comp = 0
player = 0
remain = 100


def who_starts():
    global player
    global comp
    first = random.randint(1, 2)
    if first == 1:
        player = 1
    else:
        comp = 1


who_starts()


def bot_turn(n):
    global remain
    global player
    global comp

    if remain <= 0:
        return "Игра окончена"
    if remain < 29:
        number = remain
    else:
        number = remain % 28 - 1
        if number == 0:
            number = random.randint(1, 28)
    remain -= number
    if remain == 0:
        return "Бот победил!!!!!"
    player, comp = comp, player

    return f"Бот взял {number} конфет(ы), осталось {remain} конфет(а)"


def player_turn(n):
    global remain
    global player
    global comp
    if remain <= 0:
        return "Игра окончена"
    remain -= n
    if remain == 0:
        text = "Поздравляю Вы победили!!!!!"
        return text
    player, comp = comp, player
    return f"Осталось {remain} конфет"


@bot.message_handler(commands=["start"])
def start(msg: telebot.types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    game = types.KeyboardButton("/candy")
    markup.add(game)
    bot.send_message(chat_id=msg.from_user.id, text="Choose game", reply_markup=markup)


@bot.message_handler(commands=['candy'])
def candy(msg):
    if player == 1:
        bot.send_message(chat_id=msg.from_user.id, text="Игрок ходит первым")
    else:
        bot.send_message(chat_id=msg.from_user.id, text=f"Бот ходит первым, на столе {remain} конфет")
        bot.send_message(chat_id=msg.from_user.id, text=bot_turn(remain))


@bot.message_handler()
def candy_game(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=f"На столе было {remain} конфет")
    if msg.text.isdigit():
        number = int(msg.text)
        if number > 28 or number <= 0 or number > remain:
            bot.send_message(chat_id=msg.from_user.id, text="Вы взяли неверное количество конфет, повторите попытку!")
        else:
            if player == 1:
                bot.send_message(chat_id=msg.from_user.id, text=player_turn(number))
                bot.send_message(chat_id=msg.from_user.id, text=bot_turn(remain))
            else:
                bot.send_message(chat_id=msg.from_user.id, text=bot_turn(remain))
                bot.send_message(chat_id=msg.from_user.id, text=player_turn(number))
    else:
        bot.send_message(chat_id=msg.from_user.id, text="Неверный ввод")


bot.polling()