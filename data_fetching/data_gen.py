# from postgres.insert_sample import insert_data
import random
import numpy as np
import pandas as pd

def generate_data_files(sensors:list, n_rows:int, cols:list=["value"]):
    for sensor in sensors:
        df = pd.DataFrame(np.random.rand(n_rows, len(cols)), columns=cols)
        df.to_csv(f"data/{sensor}.csv", index_label="id")


#  program that generates fake data
#  create a csv every one hour
#  load csv - validate data
#  send validated data to potamoi database
#  remove local csv
#   repeat.

# sensors = ["rainfall", "soil_moisture", "river_stage"]


# def generate_values():
#     values = []
#     dt = datetime.now()
#     # for s in range(0, 100):
#     values.append((dt, round(random.uniform(1.8, 100.99), 2)))
#     return values

# def insert_values():
#     # TODO: check tables
#     # insert data
#     for table in TABLES:
#         values = generate_values()
#         insert_data(values, table)




# def start_data_gen(target):
#     print("Starting data generation process...\n")
#     print(f"current target: {target} seconds\n")
#     target:int = target
#     seconds:int = 0
#     while seconds<target:
#         insert_values()
#         time.sleep(1)
#         seconds+=1
#         if seconds % 5 == 0:
#             print(f"Seconds left: {target-seconds}")
#     print("data generation process finished")
