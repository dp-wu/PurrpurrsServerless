from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
import os


# Setup test DB connection
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Dummy model for testing only
class DummyTable(Base):
    __tablename__ = 'dummy_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)


def test_dummy_table_creation():
    """
    Ensure SQLAlchemy can create a table in the test DB.
    """
    try:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        # Check the table exists
        from sqlalchemy import inspect
        inspector = inspect(engine)
        assert 'dummy_table' in inspector.get_table_names()
    except Exception as e:
        assert False, f"Table creation failed: {e}"
    finally:
        Base.metadata.drop_all(engine)