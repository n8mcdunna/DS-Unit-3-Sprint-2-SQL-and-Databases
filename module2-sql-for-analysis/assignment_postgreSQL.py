import psycopg2
import sqlite3
import pandas as pd


df = pd.read_csv("titanic.csv")

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

sl_conn = sqlite3.connect('test.db')
sl_curs = sl_conn.cursor()

create_table_query = """
                CREATE TABLE titanic3 (
                Survived INT,
                Pclass INT,
                Name VARCHAR,
                Sex VARCHAR,
                Age INT,
                Siblings_or_Spouses_Aboard INT,
                Parents_or_Children_Aboard INT,
                Fare FLOAT
                );
                """

#sl_curs.execute(create_table_query)

df.to_sql('titanic3', sl_conn, if_exists = 'replace', index = False)

# update_apostrophes = """
#                     UPDATE titanic3
#                     SET Name = TRIM(BOTH '"' FROM name)
#                     """

# sl_curs.execute(update_apostrophes)

passengers = sl_curs.execute("SELECT * from titanic3")

pg_curs.execute(create_table_query)

for passenger in passengers:
    pg_curs.execute(f"""
                    INSERT INTO titanic3
                    (Survived, Pclass, Name, Sex, Age, Siblings_or_Spouses_Aboard, Parents_or_Children_Aboard, Fare) 
                    VALUES
                    {passenger};""")
                    #""" + str(passenger) + ";")

pg_curs.execute('SELECT * FROM titanic3')

for row in pg_curs.fetchall()[:10]:
    print(row)

# for row in df.itertuples(index= False):
#     print(row)
#     test = [x for x in row]
#     print(test)
    #print(row[0])
    #print(row[3])
# for i in range(df.shape[1]):
#     print(df.iloc[:,i].to_string(index = False))
# print(df.head())
    # values = ()
    # for j in range(8):
    #     values += (df.iloc[i][j])
    # print(values)

#     pg_curs.execute(
#         """
#         INSERT INTO titanic 
#             (Survived, Pclass, Name, Sex, Age, Siblings_or_Spouses_Aboard, Parents_or_Children_Aboard, Fare) 
#         VALUES
#             (""" + df.iloc[i] +""")
#         """
#     )
# print(df.shape[1])
# print(df.head())
# print(df.iloc[0][1])
# print(df.iloc[0])
# print(df.iloc[1])
# print(df.loc[0])

# insert_query = """
#                 INSERT INTO titanic (name, data) VALUES
#                 (


#                 );
#                 """

# #pg_curs.execute(create_table_query)

# #pg_conn.commit()

# df.to_sql(name= 'titanic', con= pg_conn, if_exists = 'replace', index = False)
# pg_curs.execute("""
#                 SELECT *
#                 FROM titanic
#                 """)

# print(pg_curs.fetchall())