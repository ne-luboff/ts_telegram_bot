# -*- coding: utf-8 -*-
#
# Project name: tecSyntDinnerBot
# File name: environment
# Created: 2018-09-28
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>

import os

ROOT = os.path.abspath(os.path.dirname(__file__))


env = {
    'debug': True,
    'api_key': '',
    'api_pass': '',
    'cookie_secret': '',
    'password_salt': '',
    'daemon': False,
    'ssl': False,
    'port': '8989',
    'logfile': os.path.join(ROOT, 'tecSyntDinnerBot.log'),
    'pidfile': os.path.join(ROOT, 'pid'),
    'url_prefix': '',
    'site_url': 'http://localhost:8000/',
    'static_url': 'http://localhost:8000/s/',
    'serve_static': True
}