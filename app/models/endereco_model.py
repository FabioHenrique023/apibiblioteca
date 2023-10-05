from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config import Base

class Endereco_model(Base):
    __tablename__ = "endereco"
    
    id = Column(Integer, primary_key = True, autoincrement = True, index = True)
    rua = Column(String(200))
    bairro = Column(String(200))
    cep = Column(Integer)
    
    users = relationship("Users", back_populates="endereco")