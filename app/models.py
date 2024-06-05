from datetime import datetime
from sqlalchemy import Boolean, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.sql.expression import text

# from .database import Base

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(String(8), primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False,unique=True)
    password: Mapped[str] = mapped_column(String, nullable= False)
    role: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)