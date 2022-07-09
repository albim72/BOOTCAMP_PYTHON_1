#Przygotuj mini aplikację w następujący sposób:
#Stwórz klasę Pojazd (marka,model,rocznik,poj,przebieg,cena)
#Stwórz połączenie z bazą danych mysql za pomocą funcji -> conn_sql() - samodzielnie napisz
#w programie głownym połącz z przygotowaną bazą (dane połącznie takie jak login, hasło poda z input
# , zbuduj instancję klasy Pojzad i wporwadź z input dane ,
#ostatecznie wprowadzone dane zapisz jako rekord w połączonej bazie danych

from connectsql import conn_sql
from autokomis import Pojazd


print("______________")
u = input("podaj nazwę użytkownika: ")
print("______________")
p = input("podaj hasło użytkownika: ")
print("______________")
d = input("podaj nazwę bazy danych: ")
db = conn_sql(u,p,d)

mojkursor = db.cursor()
#tworzenie obiektu Pojazd
print("______________")
mrk = input("podaj markę pojazdu: ")
print("______________")
mod = input("podaj model pojazdu: ")
print("______________")
rocz = int(input("podaj rocznik: "))
print("______________")
pj = float(input("podaj pojemność [l]: "))
print("______________")
przeb = int(input("podaj przebieg [km]: "))
print("______________")
cn = float(input("podaj cenę [zł]: "))

sam = Pojazd(mrk,mod,rocz,pj,przeb,cn)


wstawrekord = "INSERT INTO pojazd(marka,model,rocznik,poj,przebieg,cena) VALUES(%s,%s,%s,%s,%s,%s)"
value = (sam.marka,sam.model,sam.rocznik,sam.poj,sam.przebieg,sam.cena)

mojkursor.execute(wstawrekord,value)

db.commit()
db.close()
