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
