from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class Tipo_usuario_schemas(BaseModel):
    id: Optional[int]=None 
    nome: Optional[str]=None 
    
    class Config:
        orm_mode = True 

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class RequestTipo(BaseModel):
    parameter : Tipo_usuario_schemas = Field(...)
    
class Response(GenericModel, Generic[T]):
    code: str
    status: str
    mensagem: str
    resultado: Optional[T]
    
class TokenResponse(BaseModel):
    access_token :str
    token_type: str