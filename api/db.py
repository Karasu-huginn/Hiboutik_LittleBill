from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
import json

def get_engine():
    with open("pg_settings.json","r") as file:
        settings = json.loads(file.read())
    db_url = f"postgresql://{settings["user"]}:{settings["pass"]}@{settings["host"]}:{settings["port"]}/{settings["db_name"]}"
    if not database_exists(db_url):
        create_database(db_url)
    return create_engine(db_url)

engine=get_engine()
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
