from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class CouponType(str, Enum):
    SPEND = "spend"
    MULTI_BUY = "multi_buy"
    ITEM = "item"
    TIERED = "tiered"

class CouponBase(BaseModel):
    chain_id: int
    is_chain_wide: bool
    coupon_type: CouponType
    description: str
    discount_amount: float
    minimum_spend: float
    start_date: datetime
    end_date: datetime
    max_uses: int

class CouponCreate(CouponBase):
    pass

class Coupon(CouponBase):
    coupon_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class CouponUpdate(CouponBase):
    pass
