from typing import Generic, Optional, List, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class Userschema(BaseModel):
    id: Optional[int] = None 
    username: Optional[str] = None
    password: Optional[str] = None 
    email: Optional[str] = None 
    phone_number: Optional[str] = None 
    first_name: Optional[str] = None  
    last_name: Optional[str] = None 
    id_tabela_endereco: Optional[int] = None
    id_tabela_tipo_usuario: Optional[int] = None
    
    class Config:
        orm_mode = True

class Resquest(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class RequestUser(BaseModel):
    parameter: Userschema = Field(...)
    
class Response(GenericModel, Generic[T]):
    code: str 
    status: str 
    mensagem: str 
    resultado: Optional[T]