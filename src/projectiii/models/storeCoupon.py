import datetime
from sqlalchemy import Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class StoreCoupon(Base):
    __tablename__ = "store_coupons"

    store_coupon_id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True
    )
    store_id: Mapped[int] = mapped_column(Integer, ForeignKey("stores.store_id"))
    coupon_id: Mapped[int] = mapped_column(Integer, ForeignKey("coupons.coupon_id"))
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
