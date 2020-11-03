import pandas as pd 
import sqlite3

# df = pd.read_csv("buddymove_holidayiq.csv")
# df.head() 
# print(df.head())

# conn = sqlite3.connect("buddymove_holidayiq.sqlite3")
# curs = conn.cursor()

# df.to_sql(name= "review", con = conn)


#if __name__ == "__main__":

NUMBER_OF_ROWS = """
    SELECT COUNT(*)
    FROM REVIEW;
    """
NATURE_AND_SHOPPER_REVIEWERS = """
    SELECT COUNT(*)
    FROM review
    WHERE review.Nature >= 100 AND review.Shopping >= 100
    """
AVERAGE_REVIEWS_PER_CATEGORY = """
    
    """
REVIEW_QUERIES = {
        "NUMBER_OF_ROWS": NUMBER_OF_ROWS,
        "NATURE_AND_SHOPPER_REVIEWERS":NATURE_AND_SHOPPER_REVIEWERS,
        "AVERAGE_REVIEWS_PER_CATEGORY":AVERAGE_REVIEWS_PER_CATEGORY
        }



conn = sqlite3.connect("buddymove_holidayiq.sqlite3")
curs = conn.cursor()

for name, query in REVIEW_QUERIES.items():
    results = pd.DataFrame(curs.execute(query))
    print(name)
    print(results)