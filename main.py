from postgres.insert_sample import insert_data
from tqdm import tqdm
import time
from datetime import datetime
from postgres.fetch_sample import get_sample
from postgres.delete_data import reset_table, delete_csv
from postgres.download_data import download_data
import random


#  program that generates fake data
#  create a csv every one hour
#  load csv - validate data
#  send validated data to potamoi database
#  remove local csv
#   repeat.

TABLES = ["rainfall", "soil_moisture", "river_stage"]


def generate_values():
    values = []
    dt = datetime.now()
    for s in range(0, 100):
        values.append((dt, round(random.uniform(1.8, 100.99), 2)))
    return values

def insert_values():
    # TODO: check tables
    # insert data
    for table in TABLES:
        values = generate_values()
        insert_data(values, table)

# def main():
#     for second in tqdm(range(5)):
#         insert_values()
#         # time.sleep(1)
#     for table in TABLES:
#         get_sample(table)
#         download_data(table)
#         reset_table(table)
#
# if __name__ == '__main__':
#     main()
