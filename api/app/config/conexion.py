from sqlalchemy import create_engine, MetaData
import pymysql
engine = create_engine("mysql+pymysql://root:admin@host.docker.internal:3306/proyectoind")

meta = MetaData()