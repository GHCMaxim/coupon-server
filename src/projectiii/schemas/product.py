from pydantic import BaseModel
from datetime import datetime

class ProductBase(BaseModel):
    store_id: int
    product_name: str
    price: float
    category_id: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    product_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class ProductUpdate(ProductBase):
    pass
