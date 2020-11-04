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
print(df.head())
df.to_sql(name= "test", con= pg_conn)
pg_conn.commit()
pg_curs.execute('SELECT * FROM TITANIC')
print(pg_curs.fetchall())