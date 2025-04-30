from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DummyTable(Base):
    __tablename__ = "dummy"
    id = Column(Integer, primary_key=True)
    message = Column(String, nullable=False)