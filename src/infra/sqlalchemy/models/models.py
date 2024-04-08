from sqlalchemy import Column, Integer, String
from src.infra.sqlalchemy.config.database import Base


class Link(Base):
    __tablename__ = 'link'

    id = Column(Integer, primary_key=True, index=True)
    original_link = Column(String)
    short_link = Column(String, unique=True)
    counter = Column(Integer, default=0)