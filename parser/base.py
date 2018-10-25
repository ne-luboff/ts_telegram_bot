# -*- coding: utf-8 -*-
#
# Project name: tecSyntDinnerBot
# File name: base
# Created: 2018-10-24
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

email = 'telegramdinnerbot@gmail.com'
password = 'qwertybot'


def main():
    CredName = "TSDinnerBot-3890ce0cdafe.json"
    PathToCred = os.path.join(os.path.dirname(os.path.abspath(__file__)), CredName)
    credentials = ServiceAccountCredentials.from_json_keyfile_name(PathToCred, scope)
    gc = gspread.authorize(credentials)
    url = "https://docs.google.com/spreadsheets/d/1HsFpm2j1v74tgRRnjE7iHjkEV8QD0TnNODTDLLfBXqE/edit#gid=445964749"
    sht2 = gc.open_by_url(url)
    return sht2

if __name__ == '__main__':
    print(main())