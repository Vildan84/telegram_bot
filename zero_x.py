import random
import telebot.types
from telebot import TeleBot
from telebot import types
import config
import emoji
bot = TeleBot(config.TOKEN)

board = {1: emoji.emojize(":keycap_1:"), 2: emoji.emojize(":keycap_2:"), 3: emoji.emojize(":keycap_3:"),
         4: emoji.emojize(":keycap_4:"), 5: emoji.emojize(":keycap_5:"), 6: emoji.emojize(":keycap_6:"),
         7: emoji.emojize(":keycap_7:"), 8: emoji.emojize(":keycap_8:"), 9: emoji.emojize(":keycap_9:")}

new_board = {1: emoji.emojize(":keycap_1:"), 2: emoji.emojize(":keycap_2:"), 3: emoji.emojize(":keycap_3:"),
             4: emoji.emojize(":keycap_4:"), 5: emoji.emojize(":keycap_5:"), 6: emoji.emojize(":keycap_6:"),
             7: emoji.emojize(":keycap_7:"), 8: emoji.emojize(":keycap_8:"), 9: emoji.emojize(":keycap_9:")}
player_x = 1
player_zero = 1
count = 0


def who_first():
    global player_x
    global player_zero
    first = random.randint(1, 2)
    if first == 1:
        player_zero = 2
    else:
        player_x = 2


who_first()


def check_result(d):
    check = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
    for e in check:
        if d[e[0]] == d[e[1]] == d[e[2]]:
            return True
    return False


def move_x(number):
    global count
    global player_x
    global player_zero

    if number > 9 or number < 0 or board[number] == "X" or board[number] == "O":
        return "Ячейка занята или число вне диапазона"
    board[number] = emoji.emojize(':cross_mark:')
    count += 1
    if count >= 5:
        if check_result(board):
            return "Победил игрок X !!! Нажмите '/clear' для очистки доски"
    if count >= 8:
        return "Ничья !!! Нажмите '/clear' для очистки доски"
    player_x, player_zero = player_zero, player_x
    return number


def move_zero(number):
    global count
    global player_x
    global player_zero
    if number > 9 or number < 0 or board[number] == "X" or board[number] == "O":
        return "Ячейка занята или число вне диапазона"
    board[number] = emoji.emojize(":hollow_red_circle:")
    count += 1
    if count >= 5:
        if check_result(board):
            return "Победил игрок O !!! Нажмите '/clear' для очистки доски"
    if count >= 8:
        return "Ничья !!! Нажмите '/clear' для очистки доски"
    player_x, player_zero = player_zero, player_x
    return number


@bot.message_handler(commands=["clear"])
def clear(msg: telebot.types.Message):
    global board
    board = new_board
    bot.send_message(chat_id=msg.from_user.id, text="Board is clear, press '/start'")


@bot.message_handler(commands=["start"])
def start(msg: telebot.types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    game = types.KeyboardButton("/zero_x")
    clean = types.KeyboardButton("/clear")
    markup.add(game, clean)
    bot.send_message(chat_id=msg.from_user.id, text="Choose game", reply_markup=markup)


@bot.message_handler(commands=['zero_x'])
def zero_x(msg):
    if player_x == 1:
        bot.send_message(chat_id=msg.from_user.id, text="Игрок X ходит первым")
        bot.send_message(chat_id=msg.from_user.id, text=f"| {board[1]} | {board[2]} | {board[3]} |")
        bot.send_message(chat_id=msg.from_user.id, text=f"| {board[4]} | {board[5]} | {board[6]} |")
        bot.send_message(chat_id=msg.from_user.id, text=f"| {board[7]} | {board[8]} | {board[9]} |")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        one = types.KeyboardButton("1")
        two = types.KeyboardButton("2")
        three = types.KeyboardButton("3")
        four = types.KeyboardButton("4")
        five = types.KeyboardButton("5")
        six = types.KeyboardButton("6")
        seven = types.KeyboardButton("7")
        eight = types.KeyboardButton("8")
        nine = types.KeyboardButton("9")
        markup.add(one, two, three, four, five, six, seven, eight, nine)
        bot.send_message(chat_id=msg.from_user.id, text="Choose number", reply_markup=markup)
    else:
        bot.send_message(chat_id=msg.from_user.id, text=f"Игрок O ходит первым")
        bot.send_message(chat_id=msg.from_user.id, text=f"| {board[1]} | {board[2]} | {board[3]} |")
        bot.send_message(chat_id=msg.from_user.id, text=f"| {board[4]} | {board[5]} | {board[6]} |")
        bot.send_message(chat_id=msg.from_user.id, text=f"| {board[7]} | {board[8]} | {board[9]} |")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        one = types.KeyboardButton("1")
        two = types.KeyboardButton("2")
        three = types.KeyboardButton("3")
        four = types.KeyboardButton("4")
        five = types.KeyboardButton("5")
        six = types.KeyboardButton("6")
        seven = types.KeyboardButton("7")
        eight = types.KeyboardButton("8")
        nine = types.KeyboardButton("9")
        markup.add(one, two, three, four, five, six, seven, eight, nine)
        bot.send_message(chat_id=msg.from_user.id, text="Choose number", reply_markup=markup)


@bot.message_handler()
def gameplay(msg: telebot.types.Message):
    if msg.text.isdigit():
        num = int(msg.text)
        if player_x == 1:
            bot.send_message(chat_id=msg.from_user.id, text=move_x(num))
            bot.send_message(chat_id=msg.from_user.id, text=f"| {board[1]} | {board[2]} | {board[3]} |")
            bot.send_message(chat_id=msg.from_user.id, text=f"| {board[4]} | {board[5]} | {board[6]} |")
            bot.send_message(chat_id=msg.from_user.id, text=f"| {board[7]} | {board[8]} | {board[9]} |")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            one = types.KeyboardButton("1")
            two = types.KeyboardButton("2")
            three = types.KeyboardButton("3")
            four = types.KeyboardButton("4")
            five = types.KeyboardButton("5")
            six = types.KeyboardButton("6")
            seven = types.KeyboardButton("7")
            eight = types.KeyboardButton("8")
            nine = types.KeyboardButton("9")
            markup.add(one, two, three, four, five, six, seven, eight, nine)
            bot.send_message(chat_id=msg.from_user.id, text="Player Zero choose number", reply_markup=markup)
        else:
            bot.send_message(chat_id=msg.from_user.id, text=move_zero(num))
            bot.send_message(chat_id=msg.from_user.id, text=f"| {board[1]} | {board[2]} | {board[3]} |")
            bot.send_message(chat_id=msg.from_user.id, text=f"| {board[4]} | {board[5]} | {board[6]} |")
            bot.send_message(chat_id=msg.from_user.id, text=f"| {board[7]} | {board[8]} | {board[9]} |")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            one = types.KeyboardButton("1")
            two = types.KeyboardButton("2")
            three = types.KeyboardButton("3")
            four = types.KeyboardButton("4")
            five = types.KeyboardButton("5")
            six = types.KeyboardButton("6")
            seven = types.KeyboardButton("7")
            eight = types.KeyboardButton("8")
            nine = types.KeyboardButton("9")
            markup.add(one, two, three, four, five, six, seven, eight, nine)
            bot.send_message(chat_id=msg.from_user.id, text="Player X choose number", reply_markup=markup)
    else:
        bot.send_message(chat_id=msg.from_user.id, text="Неверный ввод, выберете нужную ячейку")


bot.polling()