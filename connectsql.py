import mysql.connector

def conn_sql(user,passwd,database):
    return mysql.connector.connect(user=user, password=passwd,host='127.0.0.1',port=3306,database=database)
