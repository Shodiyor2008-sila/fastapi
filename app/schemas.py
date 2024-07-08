from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published:bool = True

class CreatePost(PostBase):
    pass



class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    class Config:
        from_attributes = True


class PostResponse(PostBase):
    id:int
    created_at:datetime
    user_id:int
    user:UserOut
    class Config:
        from_attributes = True


class CreateUser(BaseModel):
    # id:int
    email:EmailStr
    password:str
    created_at:datetime


class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    acces_token:str
    token_type:str
class TokenData(BaseModel):
    id:str


class Vote(BaseModel):
    post_id:int
    like: conint(le=1)



