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
