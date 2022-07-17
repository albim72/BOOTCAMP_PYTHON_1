from datetime import datetime
import sqlite3


class User:

    def __init__(self,login,password,acc_created="",acc_active="",wrong_pass_counter = 0):
        self.login = login
        self.password = password
        self.acc_created = acc_created
        self.acc_active = acc_active
        self.wrong_pass_counter =wrong_pass_counter
        self.conDB = sqlite3.connect('DB_APC.db')
