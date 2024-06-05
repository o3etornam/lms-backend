from . models import Base
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from .config import settings

# postgres connection string
SQLACHEMEY_DATABASE_URL = f"postgresql+asyncpg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"


engine = create_async_engine(SQLACHEMEY_DATABASE_URL)


async_sessionlocal = async_sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)


async def get_db():
    async with async_sessionlocal() as db:  
        yield db

async def create_all_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)