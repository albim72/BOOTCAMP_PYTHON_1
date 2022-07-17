import sqlite3
import os
from User import User
from view_controller import login_view

def cls():
    os.system('cls')

running  = True

while running:

    print("APLIKACJA AUKCJE KOMPUTEROWE: proszę się zalogować lub zarejestrować...."
          "\n1 - zaloguj się"
          "\n2 - zarejestruj się"
          "\n3 - wyjdź z programu")

    try:
        menu = int(input("wybierz opcję:\n"))
        cls()

        if menu == 1:
            login =input("login: ")
            password = input("password: ")
            cls()
            user = User(login, password)
            login_result = user.login_to_app()
            if login_result == 0:
                login_view(user)
                
            elif login_result == 1:
                pass
            elif login_result == 2:
                pass
            elif login_result == 3:
                pass
            
        elif menu == 2:
            login = input("login: ")
            password = input("password: ")
            user = User(login, password)
            
            if user.create_account() == 1:
                print("konto utworzono!")
            else:
                print("login istnieje, konto nie zotało utworzone!")
                
        elif menu == 3:
            running = False
        elif menu == 44:
            adm_menu = int(input("opcje administratora: "
                      "\n1 odblokuj użytkownika"
                      "\n4 Wyjdź\n"))
            if adm_menu == 1:
                locked_accounts = []
                conDB = sqlite3.connect('DB_APC.db')
                query = "SELECT LOGIN " \
                        "FROM Users " \
                        "WHERE ACC_ACTIVE = 0"
                cur = conDB.cursor()
                for row_log in cur.execute(query):
                    locked_accounts.append("".join(row_log))
                    
                locked_accounts.sort()
                for array_login_index in range(len(locked_accounts)):
                    print(array_login_index,": ",locked_accounts[array_login_index])
                    
                unlock_account = input("wpisz nazwę użytkownika, ktoróego chcesz odblkować: \n")
                if unlock_account in locked_accounts:
                    cur.execute("UPDATE Users "
                                "SET COUNTER_FAILED_LOGIN = 0, ACC_ACTIVE = 1 "
                                "WHERE LOGIN = ?",[unlock_account])
                    conDB.commit()
                else:
                    cls()
                    print("podano zły login!\n")
                conDB.close()
                
            elif adm_menu == 2:
                pass
            
    except ValueError:
        pass
    
    
