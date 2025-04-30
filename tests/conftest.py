import os
import pytest

# ✅ Set environment BEFORE importing anything else
os.environ["ENV"] = "test"

from database.models import Base
from database.db_connection import engine

@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    print("\n🔧 Creating schema...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("✅ Schema created.")
    yield
    print("\n🧹 Skipping dropping schema...")
    Base.metadata.drop_all(bind=engine)
    engine.dispose()
    print("✅ Done.")