from functions import sell_item, show_my_item, end_auction,delete_auction,view_item,call_item,buy_item

def login_view(user):

    bool_logged_user = True
    while bool_logged_user:
        try:
            menu = int(input("Wybierz opcję: "
                             "\n1 Mój Profil"
                             "\n2 Zobacz aukcje"
                             "\n3 Wystaw sprzęt komputerowy"
                             "\n4 Zobacz mloje whystawione przedmioty"
                             "\n5 Wyloguj się\n"))
            if menu == 1:
                menu_profile = int(input("Profil użytkownika, wybierz akcję:"
                                         "\n1 - Zmiana loginu "
                                         "\n2 - zmiana hasła "
                                         "\n3 - Wyjście\n"))
                if menu_profile == 1:
                    new_login = input("Wprowadź nowy login:\n")
                    user.change_login(new_login)
                    bool_logged_user = False
                elif menu_profile == 2:
                    new_password = input("Wprowadź nowe hasło:\n")
                    user.change_password(new_password)
                    bool_logged_user = False
                elif menu_profile == 3:
                    pass
            elif menu == 2:
                auction_view(user)
                
            elif menu == 3:
                sell_item(user)
            elif menu == 4:
                my_auctions(user)
            elif menu == 5:
                bool_logged_user = False
        except ValueError:
            pass
        
        def auction_view(user):
    running = True
    item_index = 0

    while running:
        id_item = view_item(user,item_index)
        try:
            menu_my_auctions = int(input("Wybierz akcję: "
                             "\n1 Kup"
                             "\n2 Zalicytuj"
                             "\n3 Następna aukcja"
                             "\n4 Wyjdź\n"))

            if menu_my_auctions == 1:
                buy_item(user,id_item)
            elif menu_my_auctions == 2:
                call_item(user,id_item)
            elif menu_my_auctions == 3:
                if id_item !=0:
                    item_index += 1
                else:
                    item_index = 0
                    print("to był ostatni przedmiot!")
            elif menu_my_auctions == 4:
                running = False

        except ValueError:
            pass


def my_auctions(user):
    running = True
    item_index = 0

    while running:
        id_item = show_my_item(user,item_index)
        try:
            menu_my_auctions = int(input("Wybierz akcję: "
                      "\n1 Zakończ aukcję"
                      "\n2 Usuń aukcję"
                      "\n3 Następna moja aukcja"
                      "\n4 Wyjdź\n"))
            if menu_my_auctions == 1:
                end_auction(user,id_item)
            elif menu_my_auctions == 2:
                delete_auction(user,id_item)
            elif menu_my_auctions == 3:
                if id_item !=0:
                    item_index += 1
                else:
                    item_index = 0
                    print("to był ostatni przedmiot!")
            elif menu_my_auctions == 4:
                running = False

        except ValueError:
            pass
