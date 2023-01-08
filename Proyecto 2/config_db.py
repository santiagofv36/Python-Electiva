from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

'''
    Se crea el motor de la base de datos, se le pasa la ruta de la base de datos
'''
SQLALCHEMY_DATABASE_URL = "sqlite:///./chinook.db" 
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

'''
    Se crea una sesion de la base de datos
'''
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

'''
    Se crea la base de datos
'''
Base = declarative_base()

