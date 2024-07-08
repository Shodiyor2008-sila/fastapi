from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import schemas,models,utils,database,oauth2
router = APIRouter(tags=['Authentication'])

# @router.post('/login')
# def login(user_cred:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(database.get_db)):
#     user = db.query(models.Users).filter(models.Users.email == user_cred.username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='User Not Found')
#     if not utils.verify(user_cred.password,user.password):
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Password is incorrect')
#     acces_token = oauth2.create_acces_token(data={'user_id':user.id})
#     return {'acces_token':acces_token,'token_type':'bearer'}
    # return {'status':'succes'}


@router.post('/login')
def login(user_cred: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.Users).filter(models.Users.email == user_cred.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='User Not Found')
    
    if not utils.verify(user_cred.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Password is incorrect')
    
    access_token = oauth2.create_acces_token(data={'user_id': user.id})
    return {'access_token': access_token, 'token_type': 'bearer'}
    