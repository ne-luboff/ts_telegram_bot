# -*- coding: utf-8 -*-
#
# Project name: tecSyntDinnerBot
# File name: router
# Created: 2018-09-28
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>

from handlers import IndexHandler


def api_handlers():
    return [
        (r"/", IndexHandler)
    ]