# import sqlalchemy as faloodeh_sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm.session import sessionmaker

# database+library://username:password@host:port/database_name

Model = declarative_base()   


def engine(uri = 'sqlite:///database.db'):
    engine = create_engine(uri)
    return engine

def migrate_db(engine):   
    Model.metadata.create_all(engine) 

def session(bind):
    return sessionmaker(bind=bind)()



    