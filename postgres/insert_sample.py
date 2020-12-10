import psycopg2
from postgres.config import config
from datetime import datetime
import random
# import time

# Testing postgres
def insert_data(values, table):
    """ insert a new sample into table """
    sql_query = f"INSERT INTO {table} (ID, VALUE) VALUES (%s, %s)"
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
            # print("PostgreSQL connection is closed")

# if __name__ == '__main__':
#     tables = ["rainfall", "soil_moisture", "river_stage"]
#     values = []
#     for i in range(50):
#         dt = datetime.now()
#         values.append((dt, round(random.uniform(1.8, 100.99), 2)))
#         # time.sleep(1)
#
#     print("Select the table: ")
#     for t, r in zip(tables, range(0, 3)):
#         print(r, end=" - ")
#         print(t, end=" ")
#     num = int(input("\n0, 1 or 2?: "))
#     insert_data(values, tables[num])
#     print(f"{tables[num]} updated!")
