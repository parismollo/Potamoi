from sqlalchemy import create_engine , inspect
import pymysql
import sys
import os
# from config import Config
# from api.routes import app

# app.config.from_object(Config)

def connect_db():
    try:
        sqlEngine = create_engine("postgres://hxetmggocnqbwo:df4b2b22a0a50c7ec24278cbab7166543326f5282759659ee14edc3996321c32@ec2-99-81-238-134.eu-west-1.compute.amazonaws.com:5432/d2qcvkc04p22jl", pool_recycle=3600)
        dbConnection = sqlEngine.connect()

    except Exception as i:
        print("ERROR CONNECT TO DB !")
        print("ERROR : " + str(i))
        sys.exit(84)

    return sqlEngine, dbConnection
