import psycopg2
from config import config

def get_sample(table):
    """ query sample data from the rainfall table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT id, value FROM {table} ORDER BY value")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(f"{row[0]} - {row[1]}")
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    tables = ["rainfall", "soil_moisture", "river_stage"]
    print("Select the table: ")
    for t, r in zip(tables, range(0, 3)):
        print(r, end=" - ")
        print(t, end=" ")
    num = int(input("\n0, 1 or 2?: "))
    get_sample(tables[num])
