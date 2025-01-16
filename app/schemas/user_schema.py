from pydantic import BaseModel, ConfigDict, EmailStr


class User(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    id: int | None = None
    name: str
    email: EmailStr
