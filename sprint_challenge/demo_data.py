import sqlite3

conn = sqlite3.connect("demo_data.sqlite3")
curs = conn.cursor()


create_table_query = """
    CREATE TABLE IF NOT EXISTS demo (
        s VARCHAR,
        x INT,
        y INT
    );
    """
curs.execute(create_table_query)

# curs.execute("DELETE FROM demo")

data = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
]

# for row in data:
#     curs.execute(f"""
#         INSERT INTO demo
#         (s, x, y)
#         VALUES
#         {row};
#         """)

# conn.commit()

curs.execute("SELECT * FROM demo")

for row in curs.fetchall():
    print(row)

# Count number of rows
print("count of rows:", list(curs.execute("SELECT COUNT(*) FROM demo")))

# How many rows are there where both `x` and `y` are at least 5?
xy_query = """
    SELECT COUNT(*)
    FROM demo
    WHERE x >= 5 AND y >= 5;"""
print("xy >= 5:", list(curs.execute(xy_query)))
# How many unique values of `y` are there (hint - `COUNT()` can accept a keyword
#  `DISTINCT`)?
num_y_distinct = """
    SELECT COUNT(DISTINCT y)
    FROM demo
    """
print("distinct y's:", list(curs.execute(num_y_distinct)))

curs.close()

"""
OUTPUT FROM PYTHON REPL
python demo_data.py
('g', 3, 9)
('v', 5, 7)
('f', 8, 7)
count of rows: [(3,)]
xy >= 5: [(2,)]
distinct y's: [(2,)]
"""