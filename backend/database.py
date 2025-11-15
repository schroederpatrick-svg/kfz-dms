from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# PostgreSQL Verbindungsdaten (Docker Compose)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://kfz_user:kfz_pass@db:5432/kfz_dms"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency für FastAPI-Routen
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
