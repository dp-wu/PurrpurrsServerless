from database.db_connection import SessionLocal
from database.models import DummyTable

def test_insert_and_query_dummy():
    db = SessionLocal()
    try:
        dummy = DummyTable(message="Hello test DB!")
        db.add(dummy)
        db.commit()
        db.refresh(dummy)
        result = db.query(DummyTable).first()
        assert result.message == "Hello test DB!"
    finally:
        db.close()
        # SessionLocal.remove()