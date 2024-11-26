import datetime
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class Store(Base):
    __tablename__ = "stores"

    store_id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    chain_id: Mapped[int] = mapped_column(Integer, ForeignKey("chains.chain_id"))
    store_name: Mapped[str] = mapped_column(String, unique=True, index=True)
    address: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
