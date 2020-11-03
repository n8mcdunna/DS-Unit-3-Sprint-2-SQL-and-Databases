import sqlite3
import pandas as pd
from queries import RPG_QUERIES

def connect_to_db(db = "rpg_db.sqlite3"):
    return sqlite3.connect(db)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()
    for name, query in RPG_QUERIES.items():
        results = pd.DataFrame(data = execute_query(curs, query))
        if results.shape == (1,1):
            print(name, ":", results.iloc[0,0])
        else:
            print(name)
            print(results)

