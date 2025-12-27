from db_config import Base, engine
from sqlalchemy import Column, Integer, String

class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True)
    author = Column(String(100))
    name = Column(String(100))
    path = Column(String(500))

# Создание всех моделей которые наследуются от Base
Base.metadata.create_all(engine)