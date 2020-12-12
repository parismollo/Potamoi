import os
import psycopg2
from postgres.config import config

def reset_table(table):
    """ delete all rows from table """
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(f"DELETE FROM {table}")
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print(f"The {table} table is now empty.")


def delete_csv(path):
    if os.path.exists(path):
        print(f"File {path} removed")
        os.remove(path)
    else:
        print("The file does not exist")

# if __name__ == '__main__':
#     tables = ["rainfall", "soil_moisture", "river_stage"] #TODO: create a function for this part, it can be reused elsewhere
#     print("Select the table: ")
#     for t, r in zip(tables, range(0, 3)):
#         print(r, end=" - ")
#         print(t, end=" ")
#     num = int(input("\n0, 1 or 2?: "))
#     reset_table(tables[num])
