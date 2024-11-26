from datetime import datetime
from pydantic import BaseModel

class StoreCouponBase(BaseModel):
    store_id: int
    coupon_id: int
    
class StoreCouponCreate(StoreCouponBase):
    pass

class StoreCoupon(StoreCouponBase):
    store_coupon_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class StoreCouponUpdate(StoreCouponBase):
    pass
