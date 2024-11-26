import datetime
from sqlalchemy import ForeignKey, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class CouponItem(Base):
    __tablename__ = "coupon_items"

    coupon_item_id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True
    )
    coupon_id: Mapped[int] = mapped_column(Integer, ForeignKey("coupons.coupon_id"))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.product_id"))
    quantity_required: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
