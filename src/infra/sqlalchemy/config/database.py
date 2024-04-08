from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

if os.getenv('DATABASE_URL'):
    SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
else:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./urlshortener.db"
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def criar_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()