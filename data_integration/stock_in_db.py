# from sqlalchemy import create_engine , inspect
# import pymysql
# import pandas as pd
# import numpy as np
# from data_integration.connect_db import connect_db
#
# def stock_in_database(dataFrame,tableName):
#     sqlEngine , dbConnection = connect_db()
#
#     try:
#         frame = dataFrame.to_sql(tableName, dbConnection, if_exists='replace');
#         result = sqlEngine.execute(f'SELECT * FROM {tableName}')
#         print(result.fetchall())
#
#     except ValueError as vx:
#         print(vx)
#
#     except Exception as ex:
#         print(ex)
#
#     else:
#         print("Table %s created successfully."%tableName);
#
#     finally:
#         dbConnection.close()
