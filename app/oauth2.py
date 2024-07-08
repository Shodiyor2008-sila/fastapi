from jose import jwt,JWTError
from datetime import datetime,timedelta,UTC
from fastapi import HTTPException,status,Depends
from . import schemas,database,models
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
from .config import settings


# SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
# ALGORITHM = 'HS256'
# ACCES_TOKEN_EXPIRE_MINUTES = 30

# def create_acces_token(data:dict):
#     to_encode = data.copy()
#     expire = datetime.now() + timedelta(minutes=ACCES_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({'exp':expire})
#     encoded_jwt = jwt.encode(to_encode,SECRET_KEY,ALGORITHM)
#     return encoded_jwt
# def verify_acces_token(token:str,credentionals_exception):
#     try:
#         payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
#         id:str = payload.get('user_id')
#         if not id:
#             raise credentionals_exception
#         token_data = schemas.TokenData(id=id)
#     except JWTError:
#         raise credentionals_exception
#     return token_data
# def get_current_user(token:str = Depends(oauth2_scheme)):
#     credentionals_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Could not validate credentials',headers={'WWW-Authenticate':'Bearer'})
#     return verify_acces_token(token,credentionals_exception)



SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCES_TOKEN_EXPIRE_MINUTES = settings.acces_token_expire_minutes

def create_acces_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCES_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt

def verify_acces_token(token: str, credentionals_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get('user_id')
        if not user_id:
            raise credentionals_exception
        token_data = schemas.TokenData(id=str(user_id))  # Преобразование user_id в строку
    except JWTError:
        raise credentionals_exception
    return token_data

def get_current_user(token: str = Depends(oauth2_scheme),db:Session = Depends(database.get_db)):
    credentionals_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials'
    )
    token = verify_acces_token(token, credentionals_exception)
    user = db.query(models.Users).filter(models.Users.id == token.id).first()
    return user
