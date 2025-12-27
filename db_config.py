from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# ORM - это инструмент который позволяет работать с БД
# без SQL-кода

engine = create_engine("sqlite:///db.sqlite")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()