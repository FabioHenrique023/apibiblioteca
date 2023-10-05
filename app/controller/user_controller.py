from typing import TypeVar, Generic, Optional
from sqlalchemy.orm import Session

from passlib.context import CryptContext

from datetime import datetime, timedelta
from jose import JWSError, jwt 
from config import SECRET_KEY, ALGORITHM

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException

from models.user_model import Users
from schemas.user_schema import Userschema

#criptografia da senha
pwd_cripto = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Users).offset(skip).limit(limit).all()

def get_user_id(db: Session, id: int):
    resultado = db.query(Users).filter(Users.id == id).first()
    
    if resultado is None:
        return None
    
    return resultado

def create_user(db:Session, user_create = Userschema):
    _user = Users(username = user_create.username, 
                  password = pwd_cripto.hash(user_create.password),
                  email = user_create.email,
                  phone_number = user_create.phone_number,
                  first_name = user_create.first_name,
                  last_name = user_create.last_name,
                  id_tabela_endereco = user_create.id_tabela_endereco,
                  id_tabela_tipo_usuario = user_create.id_tabela_tipo_usuario)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user

def delete_user(db:Session, id:int):
    _user = get_user_id(db=db, id=id)
    db.delete(_user)
    db.commit()
    
def update_user(db:Session, 
                    id=int, 
                    username = str, 
                    password = str,
                    email = str,
                    phone_number = str,
                    first_name = str,
                    last_name = str,
                    id_tabela_endereco = int,
                    id_tabela_tipo_usuario = int
                ):
    _user = get_user_id(db=db, id=id)
    
    if _user is None:
        return None 
    
    _user.username = username
    _user.password = pwd_cripto.hash(password)
    _user.email = email
    _user.phone_number = phone_number
    _user.first_name = first_name
    _user.last_name = last_name
    _user.id_tabela_endereco = id_tabela_endereco
    _user.id_tabela_tipo_usuario = id_tabela_tipo_usuario
    db.commit()
    db.refresh(_user)
    return _user

def busca_by_name(db: Session, username: str):
    return db.query(Users).filter(Users.username == username).first()

#LOGICA DE AUTENTICAÇÃO COM JWT

class JWTRepo():

    def generate_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        
        return encode_jwt

    def decode_token(token: str):
        try:
            decode_token = jwt.decode(token, SECRET_KEY, algorithm=[ALGORITHM])
            return decode_token if decode_token["expires"] >= datetime.time() else None
        except:
            return{}


class JWTBearer(HTTPBearer):

    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)

        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="autenticação inválido.")
            if self.verfity_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail="Token inválido ou token expirado.")
            return credentials.credentials
        else:
            raise HTTPException(
                status=403, detail="Código de autorização inválido.")

    def verfity_jwt(Self, jwttoken: str):
        isTokenValid: bool = False

        try:
            payload = jwt.decode(jwttoken, SECRET_KEY, algorithm=[ALGORITHM])
        except:
            payload = None

        if payload:
            isTokenValid = True
        return isTokenValid