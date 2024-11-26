from datetime import datetime
from pydantic import BaseModel

class ShopperCouponBase(BaseModel):
    shopper_id: int
    coupon_id: int
    is_redeemed: bool
    saved_at: datetime
    redeemed_at: datetime

class ShopperCouponCreate(ShopperCouponBase):
    pass

class ShopperCoupon(ShopperCouponBase):
    shopper_coupon_id: int

    class Config:
        orm_mode = True

class ShopperCouponUpdate(ShopperCouponBase):
    pass
