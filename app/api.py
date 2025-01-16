from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from domain.entities.user_entities import User
from domain.usecases.users.usecases import create_user
from infrastructure.adapters import get_db
from schemas.user_schema import User as UserSchema

router = APIRouter()

@router.get("")
def get():
    return {"message": "Hello world!"}


@router.post("/users/", response_model=User)
def create_user_view(user: UserSchema, db: Session = Depends(get_db)):
    return create_user(user.dict(), db)
