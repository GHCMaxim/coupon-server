import enum
import datetime
from sqlalchemy import Integer, String, Enum, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class UserRole(enum.Enum):
    SHOPPER = "shopper"
    EMPLOYEE = "employee"
    MANAGER = "manager"


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
