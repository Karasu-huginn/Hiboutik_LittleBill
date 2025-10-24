from datetime import UTC, timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from db import get_db
from models import Users
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from dotenv import load_dotenv
import os

load_dotenv()
hash_key = os.getenv("HASH_KEY")
hash_algo = os.getenv("HASH_ALGO")

router = APIRouter(prefix="/auth", tags=["auth"])
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

class CreateUserRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

db_dep = Annotated[Session, Depends(get_db)]

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(db:db_dep, create_user_request: CreateUserRequest):
    if db.query(Users).filter(Users.username == create_user_request.username).first():
        raise HTTPException(status_code=409, detail="An account with this username already exists.")
    create_user_model = Users(
        username=create_user_request.username,
        password=bcrypt_context.hash(create_user_request.password)
        )
    db.add(create_user_model)
    db.commit()

@router.post("/token", response_model=Token)
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dep):
    user = auth_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication.")
    token = create_access_token(user.username, user.id, timedelta(hours=1))
    return {"access_token":token, "token_type":"Bearer"}

def auth_user(username:str, password:str, db:db_dep):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.password):
        return False
    return user

def create_access_token(username:str, user_id:int, expiration_delta: timedelta):
    encode = {"sub": username, "id": user_id}
    expires = datetime.now(UTC) + expiration_delta
    encode.update({"exp":expires})
    return jwt.encode(encode, hash_key, algorithm=hash_algo)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, hash_key, algorithms=[hash_algo])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None :
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token.")
        return {"username":username, "id": user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token.")