"""SQLAlchemy engine, session and schema initialization."""
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from simulator_x.config import settings

Base = declarative_base()

def _engine_options(url: str):
    if url.startswith("sqlite"):
        return {"connect_args": {"check_same_thread": False}}
    return {}

engine = create_engine(settings.database_url, future=True, **_engine_options(settings.database_url))
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

def init_db():
    # Import models before create_all so SQLAlchemy registers mapped tables.
    from simulator_x.profiles.models import SIMProfile  # noqa: F401
    if settings.database_url.startswith("sqlite:///"):
        db_path = settings.database_url.removeprefix("sqlite:///")
        if db_path and db_path != ":memory:":
            Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
