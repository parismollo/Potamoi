from sqlalchemy import create_engine
import pymysql
import pandas as pd
import numpy as np

def stock_in_database(dataFrame,tableName):
    # root is your username DB
    # Password123@ is your password
    # potamois is db name
    sqlEngine = create_engine('postgres://hxetmggocnqbwo:df4b2b22a0a50c7ec24278cbab7166543326f5282759659ee14edc3996321c32@ec2-99-81-238-134.eu-west-1.compute.amazonaws.com:5432/d2qcvkc04p22jl', pool_recycle=3600)
    dbConnection = sqlEngine.connect()

    try:
        frame = dataFrame.to_sql(tableName, dbConnection, if_exists='replace');

    except ValueError as vx:
        print(vx)

    except Exception as ex:
        print(ex)

    else:
        print("Table %s created successfully."%tableName);

    finally:
        dbConnection.close()
