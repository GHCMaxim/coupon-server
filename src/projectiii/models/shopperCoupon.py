import datetime
from sqlalchemy import ForeignKey, Integer, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class ShopperCoupon(Base):
    __tablename__ = "shopper_coupons"

    shopper_coupon_id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True
    )
    shopper_id: Mapped[int] = mapped_column(Integer, ForeignKey("shoppers.shopper_id"))
    coupon_id: Mapped[int] = mapped_column(Integer, ForeignKey("coupons.coupon_id"))
    is_redeemed: Mapped[bool] = mapped_column(Boolean, default=False)
    saved_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )
    redeemed_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
