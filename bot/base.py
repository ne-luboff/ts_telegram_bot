# -*- coding: utf-8 -*-
#
# Project name: tecSyntDinnerBot
# File name: main
# Created: 2018-09-28
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>

"""Basic example for a bot that uses inline keyboards.

# This program is dedicated to the public domain under the CC0 license.
"""
from static.main import *

botToken = "631784004:AAEPd8IVE0B5JuD3FJFT5y8g93Wf2KADFZE"

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logger = logging.getLogger(__name__)

# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)
# logger = logging.getLogger(__name__)

# TODO парсить меню со страницы заказа
# TODO запоминать в кеше заказ (по айди пользователя и дню недели) или создавать запись в бд
# TODO записывать это из кеша в таблицу
# TODO научить бота его считать деньги

menu = dict()
menu['monday'] = """1	Борщ	300	12,00 грн.
2	Окрошка с курицей	300гр.	20,00 грн.
3	Суп с фрикадельками	300	22,00 грн.
4	Свекольник овощной	300	15,00 грн.
5	пюре картофельное	200	12,00 грн.
6	гречка	150	7,50 грн.
7	Овощи паровые	200	24,00 грн.
	(кап. цв.брок. .морк.фасолл спар.пер.масло раст.)
8	Каша пшеничная	150	6,00 грн.
9	рис отварной маслом	150	7,00 грн.
	вареники с мясом	200	35,00 грн.
10	Зразы с грибами	1шт.	11,00 грн.
12	Голубцы с мясом и рис	1шт	18,00 грн.
13	филе кур.отварное	100	42,00 грн.
14	Филе куриное с помидором	120	33,00 грн.
15	тефтели с мясом и рисом	100	24,00 грн.
16	котлета по-киевски	130гр.	31,00 грн.
17	Печень гов.с луком	100/10	18,00 грн.
18	котлета фаршированая сыром	100	25,00 грн.
19	Люля кебаб с говядины	100	28,00 грн.
20	Эскалоп под сыром	100	33,00 грн.
21	котлета куриная	100	22,00 грн.
22	Котлета паровая индейка	100	32,00 грн.
23	хек в яйце	100	28,00 грн.
24	котлета рыбная бужок	100	25,00 грн.
25	окорочка в медовой глазури	100гр.	25,00 грн.
26	Сырники с изюмом	1шт	7,00 грн.
27	Блинчики с мясом	1шт	10,00 грн.
	Блинчики с творогом	1шт	8,00 грн.
	Блинчик со шпин.и сыром	1шт	17,00 грн.
28	яйцо отварное	1шт.	7,00 грн.
29	сметана	50	6,00 грн.
30	С-с клубничный	40	4,00 грн.
31	Компот из сухофруктов	1бут.0,5	15,00 грн.
32	Капуста с огурцом	100гр.	8,00 грн.
33	С-т столичный	100	14,00 грн.
34	С-т слобожанский	100	11,00 грн.
35	(кап.пек.краб пал.масло раст)
36	С-т Дипломат	100гр.	9,00 грн.
37	(Свекла отв.майон.сыр)		"""

pn = [[InlineKeyboardButton("Капуста с огурцом 8grn", callback_data='32')]]


def start(bot, update):
    keyboard = [
        [InlineKeyboardButton(WeekDays[mon].capitalize(), callback_data=mon),
         InlineKeyboardButton(WeekDays[tue].capitalize(), callback_data=tue)],
        [InlineKeyboardButton(WeekDays[wed].capitalize(), callback_data=wed),
         InlineKeyboardButton(WeekDays[thu].capitalize(), callback_data=thu)],
        [InlineKeyboardButton(WeekDays[fri].capitalize(), callback_data=fri)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    # print(query)
    update.message.reply_text('Выбирай день недели:', reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query
    # print(query)
    if query.data in WeekDays.keys():
        bot.edit_message_text(
            text="О, {0} {1}! Тебя интересует {2}? Сейчас поищу меню, подожди.\n".format(query.message.chat.first_name, query.message.chat.last_name, WeekDays[query.data]),
            chat_id=query.message.chat_id,
            message_id=query.message.message_id)
        bot.send_message(chat_id=query.message.chat_id, text="{0}".format(menu['monday']))
        markup = InlineKeyboardMarkup(pn)
        bot.send_message(chat_id=query.message.chat_id, text="Когда закончишь выбирать жми /finish", reply_markup = markup)
    else:
        # markup = InlineKeyboardMarkup(pn)
        bot.send_message(chat_id=query.message.chat_id, text="Когда закончишь выбирать жми /finish")


def help(bot, update):
    update.message.reply_text("Нажми /start тыжпрограммист(ка).")


def finish(bot, update):
    update.message.reply_text('Давай проверим твой заказ:')


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def start_bot():
    # Create the Updater and pass it your bot's token.
    updater = Updater(botToken)
    logger.debug('Starting Bot: {0}'.format(updater.bot.username))
    print('Starting Bot: {0}'.format(updater.bot.username))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('finish', finish))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    start_bot()