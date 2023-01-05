from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Creamos una instacia de Engine
SQLALCHEMY_DATABASE_URL = "sqlite:///./chinook.db" 
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# este argumento: connect_args={"check_same_thread": False} es usado sólo en base de datos SQLite

# se crea una SessionLocal, que es una sesión de la base de datos:
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creamos una instancia de DeclarativeMeta
Base = declarative_base()

