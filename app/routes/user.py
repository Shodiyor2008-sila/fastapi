from .. import models,schemas,utils
from fastapi import FastAPI,Response,HTTPException,status,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List
router = APIRouter(
    prefix='/users',
    tags=['Users']
)
@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def users(user:schemas.CreateUser,db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.Users(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/{id}',response_model=schemas.UserOut)
def get_user(id:int,db:Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with id:{id} was not found')
    return user

@router.get('/',response_model=List[schemas.UserOut])
def users(db: Session = Depends(get_db)):
    post = db.query(models.Users).all()
    return post