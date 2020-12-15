# from sqlalchemy import create_engine , inspect
# import pymysql
# import pandas as pd
# import numpy as np
# from data_integration.connect_db import connect_db
#
#
# def drop_table(table):
#     sqlEngine , dbConnection = connect_db()
#     result = sqlEngine.execute(f'DROP TABLE {table[5:-4]}')
#
#
# def drop_all_tables(tables):
#     for table in tables:
#         drop_table(table)
