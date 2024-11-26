import enum
import datetime
from sqlalchemy import Integer, String, Enum, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class CouponType(enum.Enum):
    SPEND = "spend"
    MULTI_BUY = "multi_buy"
    ITEM = "item"
    TIERED = "tiered"


class Coupon(Base):
    __tablename__ = "coupons"

    coupon_id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True
    )
    chain_id: Mapped[int] = mapped_column(Integer, ForeignKey("chains.chain_id"))
    is_chain_wide: Mapped[bool] = mapped_column(Boolean, default=True)
    coupon_type: Mapped[CouponType] = mapped_column(Enum(CouponType), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    discount_amount: Mapped[float] = mapped_column(Float, nullable=False)
    minimum_spend: Mapped[float] = mapped_column(Float, nullable=True)
    start_date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    max_uses: Mapped[int] = mapped_column(Integer, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now, onupdate=datetime
    )
