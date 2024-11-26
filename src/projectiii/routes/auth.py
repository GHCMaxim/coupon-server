from datetime import datetime, timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import jwt
from sqlalchemy.orm import Session

from ..config import config
from ..routes import get_db
from .. import database, schemas
from ..schemas.auth import Token

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

auth = APIRouter(tags=["auth"])


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: int | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.secret_key, algorithm=config.algorithm)
    return encoded_jwt

@auth.post("/api/login", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    db_user = database.user.get_user_by_username(db, username = form_data.username)
    if not db_user:
        raise HTTPException(status_code=404, detail="user not found")
    if not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="incorrect username or password")
    
    access_token_expires = timedelta(minutes=float(config.access_token_expire_minutes))
    access_token = create_access_token(data={"sub": db_user.username, "role": db_user.role, "name": db_user.name}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@auth.post("/api/register", response_model=schemas.user.User)
async def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = database.user.get_user_by_username(db, username = user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username already registered")
    
    db_user = database.user.create_user(db, user=user)
    return db_user