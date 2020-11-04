import psycopg2
import sqlite3
import pandas as pd


dbname = "xhkbvohf"
user = "xhkbvohf"
password = "PZhsvlIBOiHc1hTETdHbINvrIinRfXBu"
host = "lallah.db.elephantsql.com"

pg_conn = psycopg2.connect(
                        dbname=dbname, 
                        user=user, 
                        password=password,
                        host=host)

pg_curs = pg_conn.cursor()


df = pd.read_csv("titanic.csv")
df.to_sql(name= "test", con= pg_conn)
pg_conn.commit()
pg_curs.execute('SELECT * FROM TITANIC')
print(pg_curs.fetchall())


# s1_conn = sqlite3.connect("xhkbvohf")
# s1_curs = s1_conn.cursor()



create_table_statement = """
CREATE TABLE test_table (
  id        SERIAL PRIMARY KEY,
  name  varchar(40) NOT NULL,
  data    JSONB
);
"""

insert_statement = """
INSERT INTO test_table (name, data) VALUES
(
  'A row name',
  null
),
(
  'Another row, with JSON',
  '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
);
"""

#pg_curs.execute(create_table_statement)
#pg_curs.execute(insert_statement)
#pg_conn.commit()

# query = "SELECT * FROM test_table"
# pg_curs.execute(query)
# print(pg_curs.fetchall())
# pg_curs.close()

s1_conn = sqlite3.connect("/home/n8mcdunna/lambda/Unit_3/Sprint_2_SQL/module1-introduction-to-sql/rpg_db.sqlite3")
s1_curs = s1_conn.cursor()


query = "SELECT COUNT(*) FROM charactercreator_character"
results = s1_curs.execute(query).fetchall()

# Copy characters table from SQLite to PostgreSQL
get_characters = 'SELECT * FROM charactercreator_character'
characters = s1_curs.execute(get_characters).fetchall()
#print(len(characters))

create_character_table = """
CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
);
"""
# pg_curs.execute(create_character_table)
# pg_conn.commit()

#print(characters) 

for character in characters:
    insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
    pg_curs.execute(insert_character)
pg_conn.commit()
pg_curs.execute('SELECT * FROM charactercreator_character')
print(pg_curs.fetchall())
















