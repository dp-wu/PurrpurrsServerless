import os
import pytest
from sqlalchemy import text

# ✅ Set environment BEFORE importing anything else
os.environ["ENV"] = "test"

from database.models import Base
from database.db_connection import engine

@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    print("\n🔧 Creating schema...")
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Explicitly commit the schema creation to avoid rollback
    with engine.begin() as conn:
        conn.execute(text("SELECT 1"))
    print("✅ Schema created.")
    yield

    # print("\n🧹 Dropping schema...")
    # Base.metadata.drop_all(bind=engine)
    # engine.dispose()
    # print("✅ Done.")