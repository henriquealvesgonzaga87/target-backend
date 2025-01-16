from fastapi.utils import generate_unique_id
from domain.entities.user_entities import User
from infrastructure.repositories.user_repo import UserRepository


def create_user(user_data: dict) -> User:
    user = User(user_id=generate_unique_id(), **user_data)
    user_repository = UserRepository()
    user_repository.create(user)
    return user
