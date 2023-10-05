from typing import Generic, Optional, List, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class LoginSchema(BaseModel):
    username: str
    password: str
   
    class Config:
        orm_mode = True

class ResquestL(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class RequestLogin(BaseModel):
    parameter: LoginSchema = Field(...)
    
class ResponseLogin(GenericModel, Generic[T]):
    code: str 
    status: str 
    mensagem: str 
    resultado: Optional[T]

class TokenResponse(BaseModel):
    access_token :str
    token_type: str