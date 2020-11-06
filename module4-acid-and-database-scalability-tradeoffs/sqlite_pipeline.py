""" How to create and insert data using sqlite """
import sqlite3
import pandas


def create_table(conn):
    curs = conn.cursor()
    create_statement = """
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            favorite_number INTEGER,
            least_favorite_number INTEGER
        );
    """
    curs.execute(create_statement)
    curs.close()
    curs.commit()

def insert_data(conn):
    curs = conn.cursor()
    my_data = [
        ('Tony', 2, 5),
        ('Nick', 7, 90),
        ('Donna', 4, 8),
    ]
    for data in my_data:
        pass
    
    curs.insert()
    curs.close()
    conn.commit()

if __name__ == "__main__":
    conn = sqlite3.connect("whatever_dbname_you_want.sqlite3")
    create_table(conn)
    insert_data(conn)


