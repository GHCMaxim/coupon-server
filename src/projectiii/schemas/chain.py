from pydantic import BaseModel


class ChainBase(BaseModel):
    name: str


class ChainCreate(ChainBase):
    pass


class Chain(ChainBase):
    id: int

    class Config:
        orm_mode = True
