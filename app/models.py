from datetime import datetime
from sqlalchemy import Boolean, String, DateTime, Text, ForeignKey, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.sql.expression import text

# from .database import Base

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(8), primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False,unique=True)
    password: Mapped[str] = mapped_column(String, nullable= False)
    role: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False,unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

class UserAndCourse(Base):
    __tablename__ = 'users_and_courses'

    course_id: Mapped[int] = mapped_column(Integer,  ForeignKey(column="courses.id", ondelete="cascade"), primary_key=True,nullable=False)
    user_id: Mapped[str] = mapped_column(String, ForeignKey(column="users.id", ondelete="cascade"), primary_key=True, nullable=False)