import datetime
from sqlalchemy import Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class Product(Base):
    __tablename__ = "products"

    product_id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True
    )
    store_id: Mapped[int] = mapped_column(Integer, ForeignKey("stores.store_id"))
    product_name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    category_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("categories.category_id")
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )
