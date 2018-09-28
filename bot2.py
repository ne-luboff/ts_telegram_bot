# -*- coding: utf-8 -*-
#
# Project name: tecSyntDinnerBot
# File name: bot2
# Created: 2018-09-26
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
from telegram.ext import CommandHandler, CallbackQueryHandler

BOT_TOKEN = "631784004:AAEPd8IVE0B5JuD3FJFT5y8g93Wf2KADFZE"

import telegram


HELP_BUTTON_CALLBACK_DATA = 'A unique text for help button callback data'
help_button = telegram.InlineKeyboardButton(
    text='Help me', # text that show to user
    callback_data=HELP_BUTTON_CALLBACK_DATA # text that send to bot when user tap button
    )

MENU_BUTTON_CALLBACK_DATA = 'A unique text for help button callback data'
menu_button = telegram.InlineKeyboardButton(
    text='Help me', # text that show to user
    callback_data=MENU_BUTTON_CALLBACK_DATA # text that send to bot when user tap button
    )


def command_handler_start(bot, update):
    chat_id = update.message.from_user.id
    bot.send_message(
        chat_id=chat_id,
        text='Hello. Use /help or /menu'
        # reply_markup=telegram.InlineKeyboardMarkup([help_button]),
        )


def command_handler_help(bot, update):
    chat_id = update.message.from_user.id
    bot.send_message(
        chat_id=chat_id,
        text='Help text for user ...',
        )


def command_handler_menu(bot, update):
    chat_id = update.message.from_user.id
    bot.send_message(
        chat_id=chat_id,
        text='Выбирай день недели:',
        )


def callback_query_handler(bot, update):
    cqd = update.callback_query.data
    #message_id = update.callback_query.message.message_id
    #update_id = update.update_id
    if cqd == HELP_BUTTON_CALLBACK_DATA:
        command_handler_help(bot, update)
    elif cqd == MENU_BUTTON_CALLBACK_DATA:
        command_handler_menu(bot, update)
    # elif cqd == ... ### for other buttons

update = telegram.ext.Updater(BOT_TOKEN)
bot = update.bot
dp = update.dispatcher
print('Your bot is --->', bot.username)

dp.add_handler(CommandHandler('start', command_handler_start))
dp.add_handler(CommandHandler('help', command_handler_help))
dp.add_handler(CommandHandler('menu', command_handler_menu))
dp.add_handler(CallbackQueryHandler(callback_query_handler))
update.start_polling()