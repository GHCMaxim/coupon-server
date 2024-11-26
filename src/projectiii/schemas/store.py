from datetime import datetime
from pydantic import BaseModel

class StoreBase(BaseModel):
    chain_id: int
    store_name: str
    address: str

class StoreCreate(StoreBase):
    pass

class Store(StoreBase):
    store_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class StoreUpdate(StoreBase):
    pass

