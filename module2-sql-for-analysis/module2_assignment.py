import psycopg2
import sqlite3
import pandas as pd


df = pd.read_csv("titanic.csv")
sl_conn = sqlite3.connect('example.db')

curs = sl_conn.cursor()
print(curs)