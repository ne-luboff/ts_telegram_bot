# -*- coding: utf-8 -*-
#
# Project name: tecSyntDinnerBot
# File name: utils
# Created: 2018-09-26
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>


def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu