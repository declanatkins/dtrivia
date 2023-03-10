from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import get_settings

settings = get_settings()
print(settings.DB_USER, settings.DB_PASSWORD, settings.DB_HOST, settings.DB_PORT, settings.DB_NAME)

DB_URL = f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}" \
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

engine = create_async_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base = declarative_base()


async def get_db() -> AsyncSession:
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()