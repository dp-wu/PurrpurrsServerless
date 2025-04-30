import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv

env = os.getenv("ENV", "dev")  # default to dev
dotenv_path = ".env.test" if env == "test" else ".env"
load_dotenv(dotenv_path)

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = scoped_session(sessionmaker(bind=engine))