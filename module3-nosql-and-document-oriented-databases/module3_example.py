"""How to import character table from MongoDB into SQLite"""

import sqlite3
import pymongo


PASSWORD = "87uWzvGl7uKy5k1J"
DBNAME = "test2"

def create_mdb_connection(password, dbname):
    client = pymongo.MongoClient(
        "mongodb+srv://n8mcdunna:{}@cluster0.xuszh.mongodb.net/{}?retryWrites=true&w=majority"
        .format(password, dbname)
    )
    return client

def create_sl_connection(extraction_db="/home/n8mcdunna/lambda/Unit_3/Sprint_2_SQL/module1-introduction-to-sql/rpg_db.sqlite3"):
    sl_conn = sqlite3.connect(extraction_db)
    return sl_conn

def execute_query(cursor, query):
    return cursor.execute(query).fetchall()

def character_document_creation(mdb, character_table):
    for character in character_table:
        character_document = {
            "name":character[1],
            "level":character[2],
            "exp":character[3],
            "hp":character[4],
            "strength":character[5],
            "intelligence":character[6],
            "dexterity":character[7],
            "wisdom":character[8]
        }
        mdb.insert_one(character_document)

GET_CHARACTERS = "SELECT * FROM charactercreator_character"


if __name__ == "__main__":
    sl_conn = create_sl_connection()
    sl_curs = sl_conn.cursor()
    client = create_mdb_connection(PASSWORD, DBNAME)
    db = client.test2
    characters = execute_query(sl_curs, GET_CHARACTERS)
    character_document_creation(db.test2, characters)
    print(list(db.test2.find()))