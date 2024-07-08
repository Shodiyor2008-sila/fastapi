# from passlib.context import CryptContext
# pwd_context = CryptContext(schemes=['bcrypt'],deprecated = 'auto')
# def hash(data):
#     return pwd_context.hash(data)

# def verify(plain_password,hashed_password):
#     pwd_context.verify(plain_password,hashed_password)

import bcrypt

# Hash a password using bcrypt
def hash(password):
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password

# Check if the provided password matches the stored password (hashed)
def verify(plain_password, hashed_password):
    password_byte_enc = plain_password.encode('utf-8')
    hashed_password_byte_enc = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password = password_byte_enc , hashed_password = hashed_password_byte_enc)

