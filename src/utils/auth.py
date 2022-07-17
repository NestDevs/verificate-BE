from passlib.context import CryptContext


hasher=CryptContext(schemes=["bcrypt"], deprecated=["auto"])

def hash(password:str):
    hasher.hash(password)