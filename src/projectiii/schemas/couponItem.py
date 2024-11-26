from datetime import datetime
from pydantic import BaseModel

class CouponItemBase(BaseModel):
    coupon_id: int
    product_id: int
    quantity_required: int

class CouponItemCreate(CouponItemBase):
    pass

class CouponItem(CouponItemBase):
    coupon_item_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class CouponItemUpdate(CouponItemBase):
    pass

