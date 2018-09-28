# -*- coding: utf-8 -*-
#
# Project name: tecSyntDinnerBot
# File name: bot
# Created: 2018-09-26
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils import build_menu

botToken = "631784004:AAEPd8IVE0B5JuD3FJFT5y8g93Wf2KADFZE"

# Set Up
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler



# handler functions

HELP_BUTTON_CALLBACK_DATA = 'A unique text for help button callback data'
help_button = InlineKeyboardButton(
    text='Help me', # text that show to user
    callback_data=HELP_BUTTON_CALLBACK_DATA # text that send to bot when user tap button
    )


def startCommand(bot, update):
    # bot.send_message(chat_id=update.message.chat_id, text="О, привет! Поедим? Кликай на /menu", reply_markup=InlineKeyboardMarkup([help_button]))
    bot.send_message(chat_id=update.message.chat_id, text="О, привет! Поедим? Кликай на /menu")


def textMessage(bot, update):
    # cqd = update.callback_query.data
    # print(cqd)
    response = 'Получил Ваше сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)


def buttons(bot, update):
    response = 'Получил Ваше сообщение: ' + update.message.text
    button_list = [
        InlineKeyboardButton("col1", callback_data=...),
        InlineKeyboardButton("col2", callback_data=...),
        InlineKeyboardButton("row 2", callback_data=...)
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    bot.send_message(chat_id=update.message.chat_id, text="A two-column menu", reply_markup=reply_markup)


# handlers

updater = Updater(token=botToken)
bot = updater.bot
dispatcher = updater.dispatcher
print('Your bot is --->', bot.username)

start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# button_message_handler = CommandHandler('menu', buttons)


# Добавляем хендлеры в диспетчер
dispatcher.add_handler(CommandHandler('start', startCommand))
dispatcher.add_handler(text_message_handler)
# dispatcher.add_handler(button_message_handler)


# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()