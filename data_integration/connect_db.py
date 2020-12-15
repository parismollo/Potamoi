from sqlalchemy import create_engine , inspect
import pymysql
import sys
import os
from config import Config
from api.routes import app

app.config.from_object(Config)

def connect_db():
    try:
        sqlEngine = create_engine(app.config['URL_DB'], pool_recycle=3600)
        dbConnection = sqlEngine.connect()

    except Exception as i:
        print("ERROR CONNECT TO DB !")
        print("ERROR : " + str(i))
        sys.exit(84)

    return sqlEngine, dbConnection
