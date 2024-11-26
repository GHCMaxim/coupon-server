from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    store_id: int


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True
