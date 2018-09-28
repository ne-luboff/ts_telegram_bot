# -*- coding: utf-8 -*-
#
# Project name: tecSyntDinnerBot
# File name: handler
# Created: 2018-09-28
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>

import datetime
from settings.base import BaseHandler


class IndexHandler(BaseHandler):
    allowed_methods = ('GET', )

    def get(self):
        return self.success({
            "current_time": datetime.datetime.now().isoformat()
        })