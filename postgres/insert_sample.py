import psycopg2
from config import config
from datetime import datetime
import random
import time

# Testing postgres
def insert_rainfall_sample(values): # TODO: add this feature to other tables
    """ insert a new sample into the rainfall table """
    sql_query = """ INSERT INTO rainfall (ID, VALUE)
        VALUES (%s, %s)"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        cur.executemany(sql_query, values)

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("PostgreSQL connection is closed")

# if __name__ == '__main__':
#     values = []
#     for i in range(50):
#         dt = datetime.now()
#         values.append((dt, round(random.uniform(1.8, 25.39), 2)))
#         time.sleep(1)
#
#     insert_rainfall_sample(values)
#     print("Database updated!")
