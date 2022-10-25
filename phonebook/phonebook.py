from telebot import TeleBot
from telebot import types
from add_note import add_note_to_base
from search import search_contact_in_base
from xml_generator import create_xml
from txt_generator import create_txt
from xml_import import xml_import
from txt_import import txt_import
import os
import telebot.types
import config

bot = TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def start(msg: telebot.types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    add = types.KeyboardButton("/add_contact")
    search = types.KeyboardButton("/search_contact")
    load = types.KeyboardButton("/download")
    imports = types.KeyboardButton("/import_contacts")
    export = types.KeyboardButton("/export_contacts")
    markup.add(add, search, load, imports, export)
    bot.send_message(chat_id=msg.from_user.id, text="Menu", reply_markup=markup)


@bot.message_handler(commands=["add_contact"])
def add_contact(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Введите фамилию, имя, телефон, описание")
    bot.register_next_step_handler(callback=contact, message=msg)


def contact(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=add_note_to_base(msg.text))


@bot.message_handler(commands=["download"])
def download(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Введите название документа с расширением")
    bot.register_next_step_handler(callback=sender, message=msg)


@bot.message_handler(content_types=['document'])
def sender(msg: telebot.types.Message):
    filename = "files/" + msg.text
    if os.path.exists(filename):
        bot.send_document(chat_id=msg.from_user.id, document=open(filename, 'rb'))
    else:
        bot.send_message(chat_id=msg.from_user.id, text="Файла не существует /start")


@bot.message_handler(commands=["search_contact"])
def search_contact(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Введите фамилию и имя")
    bot.register_next_step_handler(callback=sc, message=msg)


def sc(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=search_contact_in_base(msg.text))


@bot.message_handler(commands=["export_contacts"])
def export_file(msg: telebot.types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    format_xml = types.KeyboardButton("/xml")
    format_txt = types.KeyboardButton("/txt")
    markup.add(format_txt, format_xml)
    bot.send_message(chat_id=msg.from_user.id, text="Выберете формат", reply_markup=markup)


@bot.message_handler(commands=["xml"])
def xml(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Введите имя файла")
    bot.register_next_step_handler(callback=xml_export, message=msg)


def xml_export(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=create_xml(msg.text))


@bot.message_handler(commands=["txt"])
def txt(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Введите имя файла")
    bot.register_next_step_handler(callback=txt_export, message=msg)


def txt_export(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=create_txt(msg.text))


@bot.message_handler(commands=["import_contacts"])
def import_contacts(msg: telebot.types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    format_xml = types.KeyboardButton("/import_xml")
    format_txt = types.KeyboardButton("/import_txt")
    markup.add(format_txt, format_xml)
    bot.send_message(chat_id=msg.from_user.id, text="Импортируемый файл, должен находиться в папке files, "
                                                    "выберете формат файла", reply_markup=markup)


@bot.message_handler(commands=["import_xml"])
def import_xml(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Введите имя файла с расширением")
    bot.register_next_step_handler(callback=import_xml_file, message=msg)


def import_xml_file(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=xml_import(msg.text))


@bot.message_handler(commands=["import_txt"])
def import_txt(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Введите имя файла с расширением")
    bot.register_next_step_handler(callback=import_txt_file, message=msg)


def import_txt_file(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=txt_import(msg.text))


bot.polling(none_stop=True)
