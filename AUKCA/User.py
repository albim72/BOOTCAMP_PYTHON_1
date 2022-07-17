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
    #tworzenie nowego konta użytkownika
    def create_account(self):
        cur = self.conDB.cursor()
        db_login_query = []
        for row in cur.execute("SELECT LOGIN FROM Users"):
            db_login_query.append("".join(row))
            
        if self.login not in db_login_query:
            self.acc_created = datetime.date(datetime.now())
            self.acc_active = 1
            cur.execute("INSERT INTO Users(LOGIN,HASH_PASSWORD,ACC_CREATED,ACC_ACTIVE,COUNTER_FAILED_LOGIN) "
                        "VALUES (?,?,?,?,?)",(self.login, self.password, self.acc_created, self.acc_active,
                                              self.wrong_pass_counter))
            self.conDB.commit()
            return 1
        else:
            return 0
        
        
    #informacje o użytkowniku
    
    def logged_user_info(self):
        print(f"użytkownik: {self.login}, hasło: {self.password}")
        
     def __incorrect_password(self):
        cur = self.conDB.cursor()

        for row_failed_login in cur.execute("SELECT COUNTER_FAILED_LOGIN FROM Users WHERE LOGIN = ?",[self.login]):
            self.wrong_pass_counter = int(row_failed_login[0]) +1
        cur.execute("UPDATE Users SET COUNTER_FAILED_LOGIN = ? WHERE LOGIN = ?",(self.wrong_pass_counter,self.login))
        self.conDB.commit()
        
        if self.wrong_pass_counter > 3:
            cur.execute("UPDATE Users SET ACC_ACTIVE = 0 WHERE LOGIN=?",[self.login])
            self.conDB.commit()
        print("złe hasśło lub login!")
