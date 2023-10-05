from typing import List, Generic, TypeVar, Optional
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class Endereco_schema(BaseModel):
    id: Optional[int] = None
    rua: Optional[str] = None
    bairro: Optional[str] = None 
    cep: Optional[int] = None 
    
    class Config:
        orm_mode = True

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)
    
class RequestEndereco(BaseModel):
    parameter: Endereco_schema = Field(...)
    
class Response(GenericModel, Generic[T]):
    code: str 
    status: str 
    mensagem: str 
    resultado: Optional[T]