import sqlite3
from A_DigitalDevices import Device

#usuwanie przedmiotu z bazy danych i zapisywanie w pliku .txt

def buy_item(user,id_item):

    conDB = sqlite3.connect('DB_APC.db')
    user_id = user
    cur = conDB.cursor()
    query_items  = "SELECT ID, ITEM_TYPE, WEIGHT, CPU, GPU, COST " \
                   "FROM Items " \
                   "WHERE ID = ?"

    bought_item = []

    for item_info in cur.execute(query_items,[id_item]):
        bought_item.append(item_info)

    print(bought_item[0][0])

    f = open(f'{bought_item[0][0]}.txt','w')

    with open(f'{bought_item[0][0]}.txt','w') as f:
        for i in range(5):
            f.write(f"{bought_item[0][i]}")

    print("kupiono przedmiot!")
    query_delete = "DELETE FROM Items " \
                   "WHERE ID=?"
    cur.execute(query_delete,[id_item])
    
    conDB.commit()
    conDB.close()
    return 0



    conDB.commit()
    conDB.close()
    return 0

#aktualizacja licytacji -> podanie nowej kwoty i nowego licytującego,
#Uwaga! nie możesz sam przebić siebie....

def call_item(user,id_item):
    conDB = sqlite3.connect('DB_APC.db')
    cur = conDB.cursor()
    query = "SELECT ID, LAST_CALL, LAST_CALLER" \
                  "FROM Items " \
                  "WHERE ID = ?"

    called_item = []
    for item_info in cur.execute(query,[id_item]):
        called_item.append(item_info)

    my_call = int(input("Zalicytuj!\n"))

    #aktualizacja wartości w bazie: last_call oraz user, warunek: kwota jest wyższa od aktulanej a user inny
    if my_call > called_item[0][1]:
        if user.get_id() != called_item[0][2]:

            query_update = "UPDATE Items " \
                           "SET LAST_CALL = ?, LAST_CALLER = ?" \
                           "WHERE ID = ?"
            cur.execute(query_update,(my_call, user.user_id(),id_item))
            conDB.commit()
        else:
            print("Nie możesz przebićc swojej licytacji")
    else:
        print("Musisz przebić ofertę")
    conDB.close()

    #Dodawanie nowego produktu do aukcji

def sell_item(user):
    device_dict = {
        'd_type':'',
        'weight':'',
        'cpu':'',
        'gpu':'',
        'cost':''
    }
    #wprowadzenie nowego urządzenia
    try:
        d_type = input("Wprowadź typ urządzenia: ")
        cpu = input("Wprowadź nazwę procesora: ")
        gpu = input("Wprowadź nazwę karty graficznej: ")
        weight = int(input("Wprowadź wagę urządzenia w kg: "))
        cost = int(input("Wprowadź cenę towaru w pln: "))
    except ValueError:
        print('zła wartość w polu, spróbuj ponownie...')
        return 0

    new_device = Device(d_type,weight,cpu,gpu,cost,user.user_id())

    conDB = sqlite3.connect('DB_APC.db')
    cur = conDB.cursor()

    cur.execute("INSERT INTO Items (ITEM_TYPE, WEIGHT, CPU, GPU, COST, OWNED_BY) "
                "VALUES (?,?,?,?,?,?)",(new_device.item_type, new_device.weight,new_device.cpu,
                                        new_device.gpu, new_device.get_cost(),new_device.get_owner()))
    conDB.commit()
    conDB.close()

    
    #wyświetlenie dostępnych aukcji
def view_item(user,item_index):

    user_id = user.get_id()
    user_items = []

    conDB = sqlite3.connect('DB_APC.db')
    cur = conDB.cursor()
    query = "SELECT ID, ITEM_TYPE, WEIGHT, CPU, GPU, COST, LAST_CALL " \
                   "FROM Items " \
                   "WHERE OWNED_BY != ?"

    for item_info in cur.execute(query,[user_id]):
        user_items.append(item_info)

    print("____________________________________________")
    print("********** dostępne aukcje komputerowe ******************\n")

    for element_index in range(1):
        try:
            print("Typ: ", user_items[item_index][1])
            print("Waga: ", user_items[item_index][2],"kg")
            print("Procesor: ", user_items[item_index][3])
            print("Karta graficzna: ", user_items[item_index][4])
            print("Cena: ", user_items[item_index][5], "PLN")
            print("Najwyższa licytacja: ", user_items[item_index][6], "PLN")
        except IndexError:
            return 0

        element_index = 0
        conDB.close()
        return user_items[item_index][element_index]
