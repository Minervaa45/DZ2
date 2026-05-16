import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


def _build_db_url() -> str:
    url = os.getenv("DATABASE_URL")
    if url:
        return url

    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    name = os.getenv("DB_NAME", "blt")
    user = os.getenv("DB_USER", "blt")
    password = os.getenv("DB_PASSWORD", "blt")
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}"


DATABASE_URL = _build_db_url()

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
