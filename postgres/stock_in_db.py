from sqlalchemy import create_engine
import pymysql
import pandas as pd
 
def stock_in_database(dataFrame,tableName):
    # root is your username DB
    # Password123@ is your password
    # potamois is db name 
    sqlEngine = create_engine('mysql+pymysql://root:Password123@@127.0.0.1/potamoi', pool_recycle=3600)
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
 
 

        
     