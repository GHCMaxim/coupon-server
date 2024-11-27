from datetime import datetime
from sqlalchemy.orm import Session

from .. import models, schemas

def get_chain(db: Session, chain_id: int):
    return db.query(models.Chain).filter(models.Chain.chain_id == chain_id).first()

def get_chains(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Chain).offset(skip).limit(limit).all()

def create_chain(db: Session, chain: schemas.chain.ChainCreate):
    db_chain = models.Chain(
        chain_name=chain.chain_name
    )

    db.add(db_chain)
    db.commit()
    db.refresh(db_chain)

    return db_chain

def update_chain(db: Session, chain_id: int, chain: schemas.chain.ChainBase):
    db_chain = db.query(models.Chain).filter(models.Chain.chain_id == chain_id).first()
    db_chain.chain_name = chain.chain_name
    db.commit()
    db.refresh(db_chain)

    return db_chain

def get_chain_by_name(db: Session, chain_name: str):
    return db.query(models.Chain).filter(models.Chain.chain_name == chain_name).first()

