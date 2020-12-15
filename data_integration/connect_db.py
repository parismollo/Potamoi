from sqlalchemy import create_engine , inspect
import pymysql
import sys
import os

def connect_db():
    try:
        url="postgres://btdqyqwaevyiyz:719c6f9afc305abc463e0bbb57923a1acc19bc5319b81b410c235bab0754700f@ec2-174-129-199-54.compute-1.amazonaws.com:5432/d4mq2r0vpkalp0"
        sqlEngine = create_engine(url, pool_recycle=3600)
        dbConnection = sqlEngine.connect()

    except Exception as i:
        print("ERROR CONNECT TO DB !")
        print("ERROR : " + str(i))
        sys.exit(84)

    return sqlEngine, dbConnection
