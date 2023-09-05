import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


POSTGRES_USER = os.getenv('POSTGRES_USER', 'nhabe')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'hospital')
POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE', 'nhabe')
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres:5432/{POSTGRES_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
