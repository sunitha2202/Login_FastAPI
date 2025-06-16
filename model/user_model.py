from pydantic import field_validator
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_detail"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    firstname: Mapped[str] = mapped_column(String(30), nullable=False)
    lastname: Mapped[str] = mapped_column(String(30), nullable=False)
    phone: Mapped[str] = mapped_column(String(10), nullable=False)
    address: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(100), nullable=False)


    