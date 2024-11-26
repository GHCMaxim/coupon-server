from datetime import datetime
from sqlalchemy.orm import Session

from .. import models, schemas

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.category_id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

def create_category(db: Session, category: schemas.category.CategoryCreate):
    db_category = models.category.Category(
        category_name=category.category_name,
        store_id=category.store_id
    )

    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category

def update_category(db: Session, category_id: int, category: schemas.category.CategoryBase):
    db_category = db.query(models.Category).filter(models.Category.category_id == category_id).first()
    db_category.category_name = category.category_name
    db.commit()
    db.refresh(db_category)

    return db_category

def get_categories_of_store(db: Session, store_id: int):
    return db.query(models.Category).filter(models.Category.store_id == store_id).all()
