from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    email: EmailStr


class UserDB(User):
    id: int


class Userlist(BaseModel):
    users: list[UserPublic]
