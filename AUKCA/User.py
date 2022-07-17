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
    def login_to_app(self):

        cur = self.conDB.cursor()

        db_login_query = []
        db_pass_query = []

        for row_log in cur.execute("SELECT LOGIN FROM Users"):
            db_login_query.append("".join(row_log))
        if self.login not in db_login_query:
            print(f"nie ma takiego użytkownika lub hasło jest niepoprawne... - {self.login}")
            return 1

        for row_pass in cur.execute("SELECT HASH_PASSWORD FROM Users WHERE LOGIN = ?",[self.login]):
            db_pass_query.append("".join(row_pass))
        if  self.password not in db_pass_query:
            self.__incorrect_password()
            return 2

        for row_isActive in cur.execute("SELECT ACC_ACTIVE FROM Users WHERE LOGIN=?",[self.login]):
            if row_isActive[0] != 1:
                print(f"Konto: {self.login} jest zablokowane! Skontaktuj się z administratorem.")
                return 3
            
        print("logowanie poprawne...")
        return 0

    #usuwanie konta
    def delete_account(self):
        cur = self.conDB.cursor()
        cur.execute("DELETE FORM Users WHERE LOGIN = ?",[self.login])
        self.conDB.commit()
        print("profil usunięty!")
        return 1

        def change_login(self,new_login):
        cur = self.conDB.cursor()
        cur.execute("UPDATE Users SET LOGIN = ? WHERE LOGIN = ?",(new_login,self.login))
        self.conDB.commit()

    def change_password(self,new_password):
        cur = self.conDB.cursor()
        cur.execute("UPDATE Users SET HASH_PASSWORD = ? WHERE LOGIN = ?",(new_password,self.login))
        self.conDB.commit()

    def get_id(self):
        cur = self.conDB.cursor( )
        user_id = ""
        for user in cur.execute("SELECT ID FROM Users WHERE LOGIN =?",[self.login]):
            user_id = user
        return user_id[0]

    def __del__(self):
        self.conDB.close()
