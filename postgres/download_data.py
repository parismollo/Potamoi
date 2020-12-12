import sys
import psycopg2
from postgres.config import config


def download_data(table):
    """ download data from table into csv """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        output_query = f"COPY {table} TO STDOUT WITH CSV HEADER"
        file_name = f"test/results_{table}.csv"
        with open(file_name, "w") as f:
            cur.copy_expert(output_query, f)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            # print("PostgreSQL connection is closed")


def download_all_tables(tables):
    for table in tables:
        download_data(table)

# if __name__ == '__main__':
#     tables = ["rainfall", "soil_moisture", "river_stage"]
#     print("Select the table: ")
#     for t, r in zip(tables, range(0, 3)):
#         print(r, end=" - ")
#         print(t, end=" ")
#     num = int(input("\n0, 1 or 2?: "))
#
