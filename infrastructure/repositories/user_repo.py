from sqlalchemy.orm import Session
from domain.entities.user_entities import User


class UserRepository:
    def create(self, db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
