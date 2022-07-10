import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn =sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def create_table(conn,create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)



def create_project(conn,project):
    sql = """
    INSERT INTO projects(name,begin_date,end_date)
    VALUES(?,?,?)
    """
    cur = conn.cursor()
    cur.execute(sql,project)
    conn.commit()
    return cur.lastrowid

def create_task(conn,task):
    sql = """
    INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
    VALUES(?,?,?,?,?,?)
    """
    cur = conn.cursor()
    cur.execute(sql,task)
    conn.commit()
    return cur.lastrowid

def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_tasks_by_priority(conn,priority):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority = ?",(priority,))
    rows = cur.fetchall()

    for row in rows:
        print(row)


def delete_all_tasks(conn):
    sql = 'DELETE FROM tasks'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def update_task(conn,task):

    sql = """
    UPDATE tasks
    SET priority = ?,
        begin_date = ?,
        end_date = ?
    WHERE id = ?
    """
    cur = conn.cursor()
    cur.execute(sql,task)
    conn.commit()

def main():

    database = r"C:\sqlite\db\ptyhoncqlite.db"

    sql_create_projects_table = """
    CREATE TABLE IF NOT EXISTS projects (
        id integer PRIMARY KEY,
        name text NOT NULL,
        begin_date text,
        end_date text
    );
    """

    sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
        id integer PRIMARY KEY,
        name text NOT NULL,
        priority integer,
        status_id integer NOT NULL,
        project_id integer NOT NULL,
        begin_date text,
        end_date text,
        FOREIGN KEY(project_id) REFERENCES projects(id)
    );
    """
    conn = create_connection(database)

    if conn is not None:
        create_table(conn,sql_create_projects_table)
        create_table(conn,sql_create_tasks_table)
    else:
        print("Błąd!nie można nawiązać połączenia z bazą!")

    with conn:

        project = ('ciekawa aplikacja Python dla systemu Android','2022-05-23','2022-10-10')
        project_id = create_project(conn,project)

        task_1 = ('Analiza wymagań aplikacji',1,1,project_id,'2022-05-23','2022-06-15')
        task_2 = ('Konfiguracja parametrów sprzętowych na potrzeby projektu',1,1,project_id,'2022-06-02','2022-07-10')
        task_3 = ('Przydział zasobów do zadań',2,1,project_id,'2022-05-30','2022-06-27')

        create_task(conn, task_1)
        create_task(conn, task_2)
        create_task(conn, task_3)

    with conn:
        print("1. Wyniki zapytania - wszystkie zadania:")
        select_all_tasks(conn)
        print("2. Wyniki zapytania - zadania po priorytecie:")
        select_tasks_by_priority(conn, 2)

    print("Zmiana danych .......")
    with conn:
        update_task(conn,(3, '2022-08-01', '2022-09-12', 1))

    with conn:

        print("Wyniki zapytania - wszystkie zadania - po update:")
        select_all_tasks(conn)


    with conn:
        delete_all_tasks(conn)

    with conn:

        print("Wyniki zapytania - wszystkie zadania - po usunięciu:")
        select_all_tasks(conn)



if __name__ == '__main__':
    main()
